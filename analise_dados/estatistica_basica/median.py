import pandas as pd

df = pd.read_csv('C:/Projetos/estudo_pandas/netflix_titles.csv')

# Mediana do ano de lançamento
mediana = df['release_year'].median()

print(f'Mediana do ano de lançamento: {mediana}')