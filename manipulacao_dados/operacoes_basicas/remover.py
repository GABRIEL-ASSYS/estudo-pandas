import pandas as pd

df = pd.read_csv('C:/Projetos/estudo_pandas/netflix_titles.csv')

# Remover uma coluna sem modificar o DataFrame original
df_removido = df.drop(columns=['director'], axis=1)

print(df_removido.head())