import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv(r'D:\prog\Python(Narind Verma)\class exercise\netflix_titles.csv')
directors_df = df['director'].str.split(',', expand=True).stack().reset_index(level=1, drop=True).reset_index(name='director')
df_expanded = df.drop('director', axis=1).merge(directors_df, left_index=True, right_index=True)

director_country_rating = df_expanded.groupby(['director', 'country', 'rating']).size().reset_index(name='count')
plt.figure(figsize=(15, 10))
sns.barplot(data=director_country_rating.sort_values(by='count', ascending=False).head(20),
            x='director',
            y='count',
            hue='country',
            palette='viridis')
plt.title('Top 20 Directors by Rating and Country on Netflix')
plt.xlabel('Director')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()