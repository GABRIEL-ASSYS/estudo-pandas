import pandas as pd

df = pd.read_csv('C:/Projetos/estudo_pandas/netflix_titles.csv')

# Preencher valores ausentes em "rating" com 'Not Rated'
df_fillna = df.copy()
df_fillna['rating'] = df_fillna['rating'].fillna('Not Rated')

print(df_fillna[['title', 'rating']].head())