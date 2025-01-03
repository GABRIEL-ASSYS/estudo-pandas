import pandas as pd

df = pd.read_csv('C:/Projetos/estudo_pandas/netflix_titles.csv')

# Agregando a contagem de títulos por tipo
aggregado = df.groupby('type').agg({'title': 'count'})

print(aggregado)