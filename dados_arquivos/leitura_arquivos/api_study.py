import pandas as pd
import requests

url = 'https://jsonplaceholder.typicode.com/posts'

response = requests.get(url)
data = response.json()

df = pd.DataFrame(data)

print(df.head())