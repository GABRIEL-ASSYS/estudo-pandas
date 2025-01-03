import pandas as pd

df = pd.read_csv('C:/Projetos/estudo_pandas/netflix_titles.csv')

# Criando um índice de data
df_indexado = df.copy()
df_indexado['date_added'] = pd.to_datetime(df_indexado['date_added'], errors='coerce')
df_indexado.set_index('date_added', inplace=True)

print(df_indexado.head())