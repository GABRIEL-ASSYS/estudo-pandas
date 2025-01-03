import pandas as pd

df = pd.read_csv('C:/Projetos/estudo_pandas/netflix_titles.csv')

# Desvio padrão do ano de lançamento
desvio_padrao = df['release_year'].std()

print(f'Desvio padrão do ano de lançamento: {desvio_padrao}')