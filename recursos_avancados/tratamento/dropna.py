import pandas as pd

df = pd.read_csv('C:/Projetos/estudo_pandas/netflix_titles.csv')

# Remover linhas onde "date_added" está ausente
df_dropna = df.dropna(subset=['date_added'])

print(f'Linhas antes: {len(df)}')
print(f'Linhas depois: {len(df_dropna)}')