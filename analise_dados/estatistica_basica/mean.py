import pandas as pd

df = pd.read_csv('C:/Projetos/estudo_pandas/netflix_titles.csv')

# Média fictícia de anos de lançamento (excluindo NaN)
media = df['release_year'].mean()

print(f'Média do ano de lançamento: {media}')