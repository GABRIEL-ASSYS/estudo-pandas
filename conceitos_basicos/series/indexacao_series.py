import pandas as pd

df = pd.read_csv('C:/Projetos/estudo_pandas/netflix_titles.csv')

series_titles = df['title']

print(series_titles[0])
print(series_titles[:5])