import pandas as pd

titles = ['Breaking Bad', 'Narcos', 'The Witcher']
types = ['TV Show', 'TV Show', 'TV Show']
years = [2008, 2015, 2019]

df = pd.DataFrame({
    'title': titles,
    'type': types,
    'release_year': years
})

print(df)