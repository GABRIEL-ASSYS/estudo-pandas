import pandas as pd

df = pd.read_csv('C:/Projetos/estudo_pandas/netflix_titles.csv')

# Selecionar as 5 primeiras linhas e as colunas 0 a 2
subset = df.iloc[:5, :3]

print(subset)