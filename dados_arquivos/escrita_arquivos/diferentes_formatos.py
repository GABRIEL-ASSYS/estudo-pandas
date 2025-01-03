import pandas as pd

df = pd.read_csv('C:/Projetos/estudo_pandas/netflix_titles.csv')

# Exportar para um arquivo Excel
df.to_excel('netflix_titles.xlsx', index=False)

# Exportar para JSON
df.to_json('netflix_titles.json', orient='records', lines=True)

# Exportar para HTML
df.to_html('netflix_titles.html', index=False)

print("Arquivos exportados em diferentes formatos com sucesso!")