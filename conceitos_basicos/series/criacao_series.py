import pandas as pd

df = pd.read_csv('C:/Projetos/estudo_pandas/netflix_titles.csv')

series_titles = pd.Series(df['title'])
print(series_titles.head())