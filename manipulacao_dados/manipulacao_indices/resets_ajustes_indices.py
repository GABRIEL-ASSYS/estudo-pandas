import pandas as pd

df = pd.read_csv('C:/Projetos/estudo_pandas/netflix_titles.csv')

# Resetar o índice sem modificar o DataFrame original
resetado = df.reset_index()

print(resetado.head())