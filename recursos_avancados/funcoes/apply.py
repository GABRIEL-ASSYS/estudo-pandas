import pandas as pd

df = pd.read_csv('C:/Projetos/estudo_pandas/netflix_titles.csv')

# Criar uma nova coluna com o número de palavras no título
df_apply = df.copy()
df_apply['title_word_count'] = df_apply['title'].apply(lambda x: len(str(x).split()))

print(df_apply[['title', 'title_word_count']].head())