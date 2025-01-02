import pandas as pd

df = pd.read_csv('C:/Projetos/estudo_pandas/netflix_titles.csv')

df_novo = df.copy()
df_novo['title_upper'] = df_novo['title'].apply(lambda x: x.upper())

print(df_novo[['title', 'title_upper']].head())