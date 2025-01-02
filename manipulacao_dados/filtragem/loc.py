import pandas as pd

df = pd.read_csv('C:/Projetos/estudo_pandas/netflix_titles.csv')

# Selecionar títulos e anos de lançamento para os primeiros 5 itens
subset = df.loc[:4, ['title', 'release_year']]

print(subset)