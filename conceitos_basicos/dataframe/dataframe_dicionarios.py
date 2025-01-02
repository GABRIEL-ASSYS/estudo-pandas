import pandas as pd

dados = {
    'title': ['Stranger Things', 'The Crown', 'Black Mirror'],
    'type': ['TV Show', 'TV Show', 'TV Show'],
    'release_year': [2016, 2016, 2011],
    'rating': ['TV-14', 'TV-MA', 'TV-MA']
}

df = pd.DataFrame(dados)

print(df)