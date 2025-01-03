import pandas as pd

df1 = pd.DataFrame({'title': ['Movie 1', 'Movie 2'], 'year': [2020, 2021]}).set_index('title')
df2 = pd.DataFrame({'rating': ['PG', 'R']}, index=['Movie 1', 'Movie 2'])

# Fazer join dos DataFrames
combinado = df1.join(df2)

print(combinado)