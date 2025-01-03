import pandas as pd

df = pd.read_csv('C:/Projetos/estudo_pandas/netflix_titles.csv')

# Ordenar por ano de lançamento sem modificar o DataFrame original
df_ordenado = df.sort_values(by='release_year', ascending=False)

print(df_ordenado[['title', 'release_year']].head())