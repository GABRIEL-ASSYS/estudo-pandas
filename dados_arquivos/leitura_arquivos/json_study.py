import pandas as pd

file_path = 'C:/Projetos/estudo_pandas/netflix_titles.json'

df = pd.read_json(file_path, orient='records', lines=True)

print(df.head())