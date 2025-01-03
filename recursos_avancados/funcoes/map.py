import pandas as pd

df = pd.read_csv('C:/Projetos/estudo_pandas/netflix_titles.csv')

# Mapear valores para substituir tipos
df_map = df.copy()
df_map['type_mapped'] = df_map['type'].map({'Movie': 'Filme', 'TV Show': 'Programa de TV'})

print(df_map[['type', 'type_mapped']].head())