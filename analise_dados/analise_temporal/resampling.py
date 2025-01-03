import pandas as pd

df = pd.read_csv('C:/Projetos/estudo_pandas/netflix_titles.csv')

# Criando uma coluna de data para resampling
df_temporal =df.copy()
df_temporal['date_added'] = pd.to_datetime(df_temporal['date_added'], errors='coerce')
df_temporal.set_index('date_added', inplace=True)

# Contando títulos adicionados por ano
resample = df_temporal.resample('Y')['title'].count()

print(resample)