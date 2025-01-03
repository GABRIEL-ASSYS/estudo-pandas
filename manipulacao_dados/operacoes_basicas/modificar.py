import pandas as pd

df = pd.read_csv('C:/Projetos/estudo_pandas/netflix_titles.csv')

df_modificado = df.copy()

# Modificar a coluna released_year
df_modificado['release_year'] = df_modificado['release_year'].fillna(0).astype(int)

print(df_modificado[['title', 'release_year']].head(30))