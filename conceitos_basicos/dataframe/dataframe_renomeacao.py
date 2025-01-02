import pandas as pd

df = pd.read_csv('C:/Projetos/estudo_pandas/netflix_titles.csv')

df_renomeado = df.rename(columns={'release_year': 'ano_lancamento', 'type': 'tipo'})

print(df_renomeado.head())