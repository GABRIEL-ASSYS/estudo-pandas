import pandas as pd

df = pd.read_csv('C:/Projetos/estudo_pandas/netflix_titles.csv')

# Criar uma tabela pivot para contar tipos por ano de lançamento
pivot_table = df.pivot_table(
    index='release_year',
    columns='type',
    values='title',
    aggfunc='count'
)

print(pivot_table.head())