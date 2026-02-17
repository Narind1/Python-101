import torch
import torch.nn as nn
import torch.nn.functional as F
import math

class Config:
    def __init__(self):
        self.src_vocab_size = 5000
        self.tgt_vocab_size = 5000
        self.d_model = 512
        self.num_heads = 8         
        self.num_layers = 4        
        self.d_ff = 2048
        self.dropout = 0.1
        self.max_len = 100


class HybridFeatureExtractor(nn.Module):
    def __init__(self, d_model):
        super().__init__()
        self.conv = nn.Conv1d(in_channels=d_model, out_channels=d_model, kernel_size=3, padding=1)
        self.activation = nn.GELU()

    def forward(self, x):
        x = x.transpose(1, 2)
        x = self.activation(self.conv(x))
        return x.transpose(1, 2)


class LearnablePositionalEncoding(nn.Module):
    """
    Replaces the fixed Sinusoidal encoding with learnable embeddings.
    """
    def __init__(self, d_model, max_len=5000):
        super().__init__()
        self.pe = nn.Parameter(torch.randn(1, max_len, d_model))

    def forward(self, x):
        seq_len = x.size(1)
        return x + self.pe[:, :seq_len, :]


class LinearAttention(nn.Module):
    """
    Replaces Scaled Dot-Product Attention (O(N^2)) with Linear Attention (O(N)).
    Formula: (Q @ K.T) @ V  --> Q @ (K.T @ V)
    We use elu(x) + 1 as the kernel function phi(x).
    """
    def __init__(self, d_model, num_heads, dropout=0.1):
        super().__init__()
        assert d_model % num_heads == 0
        self.d_k = d_model // num_heads
        self.num_heads = num_heads
        
        self.q_linear = nn.Linear(d_model, d_model)
        self.k_linear = nn.Linear(d_model, d_model)
        self.v_linear = nn.Linear(d_model, d_model)
        self.out_linear = nn.Linear(d_model, d_model)
        
        self.dropout = nn.Dropout(dropout)

    def feature_map(self, x):
        """Kernel function phi(x) = elu(x) + 1"""
        return F.elu(x) + 1

    def forward(self, q, k, v, mask=None):
        bs = q.size(0)
        

        Q = self.q_linear(q).view(bs, -1, self.num_heads, self.d_k).transpose(1, 2)
        K = self.k_linear(k).view(bs, -1, self.num_heads, self.d_k).transpose(1, 2)
        V = self.v_linear(v).view(bs, -1, self.num_heads, self.d_k).transpose(1, 2)

        Q = self.feature_map(Q)
        K = self.feature_map(K)


        kv = torch.matmul(K.transpose(-2, -1), V)  # [bs, heads, d_k, d_k]
        z = 1 / (torch.matmul(Q, K.sum(dim=-2, keepdim=True).transpose(-2, -1)) + 1e-6)
        
        attn_output = torch.matmul(Q, kv) * z
        
        attn_output = attn_output.transpose(1, 2).contiguous().view(bs, -1, self.d_k * self.num_heads)
        return self.out_linear(attn_output)


class ModifiedEncoderLayer(nn.Module):
    def __init__(self, d_model, num_heads, d_ff, dropout):
        super().__init__()
        self.self_attn = LinearAttention(d_model, num_heads, dropout)
        self.ffn = nn.Sequential(
            nn.Linear(d_model, d_ff),
            nn.GELU(),
            nn.Linear(d_ff, d_model)
        )
        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x, mask=None):
        x2 = self.norm1(x)
        x = x + self.dropout(self.self_attn(x2, x2, x2, mask))
        x2 = self.norm2(x)
        x = x + self.dropout(self.ffn(x2))
        return x

class ModifiedTransformer(nn.Module):
    def __init__(self, config):
        super().__init__()
        self.embedding = nn.Embedding(config.src_vocab_size, config.d_model)
        
        self.pos_encoder = LearnablePositionalEncoding(config.d_model, config.max_len)
        
        self.hybrid_cnn = HybridFeatureExtractor(config.d_model)
        
        # [MODIFICATION] Configurable Depth (Number of layers)
        self.layers = nn.ModuleList([
            ModifiedEncoderLayer(config.d_model, config.num_heads, config.d_ff, config.dropout)
            for _ in range(config.num_layers)
        ])
        
        self.norm_final = nn.LayerNorm(config.d_model)
        self.fc_out = nn.Linear(config.d_model, config.tgt_vocab_size)

    def forward(self, x):
        # 1. Embeddings
        x = self.embedding(x)
        
        # 2. Hybrid Stage (CNN)
        x = self.hybrid_cnn(x)
        
        # 3. Add Position Info
        x = self.pos_encoder(x)
        
        # 4. Transformer Layers
        for layer in self.layers:
            x = layer(x)
            
        x = self.norm_final(x)
        logits = self.fc_out(x)
        return logits

# -----------------------------------------------------------------------------
# Pipeline Execution
# -----------------------------------------------------------------------------
def run_pipeline():
    # 1. Initialize Config
    cfg = Config()
    cfg.num_layers = 6  # User requested change in layers
    cfg.num_heads = 4   # User requested change in heads

    # 2. Instantiate Model
    model = ModifiedTransformer(cfg)
    print(f"Model Created with {cfg.num_layers} layers and {cfg.num_heads} heads.")
    print(f"Architecture includes Hybrid CNN and Linear Attention.")

    # 3. Dummy Input (Batch Size=2, Seq Len=10)
    src_data = torch.randint(0, cfg.src_vocab_size, (2, 10))

    # 4. Forward Pass
    output = model(src_data)
    print(f"Input shape: {src_data.shape}")
    print(f"Output shape: {output.shape}") # Should be [2, 10, vocab_size]

if __name__ == "__main__":
    run_pipeline()
