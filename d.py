import pandas as pd

df1 = pd.DataFrame({
    'A': [1, 2, 3],
    'B': ['a', 'b', 'c']
})

df2 = pd.DataFrame({
    'A': [4, 5, 6],
    'B': ['d', 'e', 'f']
})

combined_df = pd.concat([df1, df2], ignore_index=True)

print("Combined DataFrame:")
print(combined_df)
combined_df.drop(index=[0,1,2,3,4,5], inplace=True)
combined_df.drop(columns=['A', 'B'], inplace=True)

print("Modified DataFrame:")
print(combined_df)
