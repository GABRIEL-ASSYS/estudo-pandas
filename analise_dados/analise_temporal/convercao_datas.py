import pandas as pd

df = pd.read_csv('C:/Projetos/estudo_pandas/netflix_titles.csv')

# Convertendo a coluna "date_added" para datetime
df_temporal = df.copy()
df_temporal['date_added'] = pd.to_datetime(df_temporal['date_added'], errors='coerce')

print(df_temporal[['title', 'date_added']].head())