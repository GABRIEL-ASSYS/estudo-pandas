import pandas as pd

df = pd.read_csv('C:/Projetos/estudo_pandas/netflix_titles.csv')

# Criar uma indexação hierárquica com o tipo e ano de lançamento
df_hierarquico = df.set_index(['type', 'release_year'])

print(df_hierarquico.head())