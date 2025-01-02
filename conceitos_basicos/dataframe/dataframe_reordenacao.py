import pandas as pd

df = pd.read_csv('C:/Projetos/estudo_pandas/netflix_titles.csv')

df_reordenado = df[['title', 'release_year', 'type', 'rating']]

print(df_reordenado.head())