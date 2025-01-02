import pandas as pd

df = pd.read_csv('C:/Projetos/estudo_pandas/netflix_titles.csv')

filtros = df[(df['type'] == 'Movie') & (df['release_year'] > 2015)]

print(filtros[['title', 'release_year', 'type']].head())