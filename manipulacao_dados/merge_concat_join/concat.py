import pandas as pd

df = pd.read_csv('C:/Projetos/estudo_pandas/netflix_titles.csv')

df_extra = pd.DataFrame({
    'title': ['Extra Movie 1', 'Extra Movie 2'],
    'type': ['Movie', 'Movie'],
    'release_year': [2023, 2024]
})

# Concatenar os DataFrames
concatenando = pd.concat([df, df_extra], ignore_index=True)

print(concatenando.tail())