import pandas as pd

df = pd.read_csv('C:/Projetos/estudo_pandas/netflix_titles.csv')

# Verificar colunas e normalizar
df.columns = df.columns.str.strip()

ratings = pd.DataFrame({
    'rating': ['TV-MA', 'TV-14'],
    'description': ['Mature Audience', 'Teens and Up']
})

# Normalizar colunas de ratings
ratings.columns = ratings.columns.str.strip()

# Garantir que 'rating' é string
df['rating'] = df['rating'].astype(str)
ratings['rating'] = ratings['rating'].astype(str)

# Fazer o merge com controle de sufixos
merge_df = pd.merge(df, ratings, on='rating', how='left', suffixes=('_original', '_new'))

# Renomear as colunas para evitar confusões
merge_df.rename(columns={'description_new': 'description'}, inplace=True)

# Substituir NaN na coluna 'description'
merge_df['description'] = merge_df['description'].fillna('No Description Available')

print(merge_df[['title', 'rating', 'description']].head())