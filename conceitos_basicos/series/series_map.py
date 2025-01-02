import pandas as pd 

df = pd.read_csv('C:/Projetos/estudo_pandas/netflix_titles.csv')

df['title_length'] = df['title'].map(len)

print(df[['title', 'title_length']].head())