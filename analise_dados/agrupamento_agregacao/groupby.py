import pandas as pd

df = pd.read_csv('C:/Projetos/estudo_pandas/netflix_titles.csv')

# Contar número de títulos por tipo
agrupado = df.groupby('title')['title'].count()

print(agrupado)