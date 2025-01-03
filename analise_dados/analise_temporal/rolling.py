import pandas as pd

df = pd.read_csv('C:/Projetos/estudo_pandas/netflix_titles.csv')

# Criando uma coluna de data
df_temporal = df.copy()
df_temporal['date_added'] = pd.to_datetime(df_temporal['date_added'], errors='coerce')
df_temporal.set_index('date_added', inplace=True)

# Aplicando uma janela deslizante de 30 dias
rolling_count = df_temporal['title'].resample('D').count().rolling(window=30).sum()

print(rolling_count.dropna().head())