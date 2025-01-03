import pandas as pd

df = pd.read_csv('C:/Projetos/estudo_pandas/netflix_titles.csv')

df_novo = df.copy()

# Adicionar uma nova coluna ao DataFrame
df_novo['title_length'] = df['title'].apply(len)

print(df_novo[['title', 'title_length']].head())