import pandas as pd

df = pd.read_csv('C:/Projetos/estudo_pandas/netflix_titles.csv')

colunas = df[['title', 'type', 'release_year']]
print(colunas.head(10))

tv_shows = df[df['type'] == 'TV Show']
print(tv_shows.head(10))