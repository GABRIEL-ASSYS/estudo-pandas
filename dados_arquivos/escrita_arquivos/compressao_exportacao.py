import pandas as pd

df = pd.read_csv('C:/Projetos/estudo_pandas/netflix_titles.csv')

# Exportar para CSV comprimido em ZIP
df.to_csv('netflix_titles_compressed.zip', index=False, compression='zip')

# Exportar para CSV comprimido em GZIP
df.to_csv('netflix_titles_compressed.csv.gz', index=False, compression='gzip')

print("Arquivos comprimidos e exportados com sucesso!")