pip install beautifulsoup4 requests

______________________


import requests
from bs4 import BeautifulSoup
import json

______________________

url = 'https://example.com'
resposta = requests.get(url)
soup = BeautifulSoup(resposta.content, 'html.parser')

# Extrair títulos de artigos como exemplo
titulos = soup.find_all('h2', class_='titulo-artigo')
for titulo in titulos:
    print(titulo.get_text())


______________________


api_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
resposta_api = requests.get(api_url)
dados_api = resposta_api.json()

# Exibir o preço atual do Bitcoin
print("Preço Atual do Bitcoin (USD):", dados_api['bpi']['USD']['rate'])

______________________


# Exemplo: salvar os títulos de artigos e o preço do Bitcoin em um arquivo JSON
dados_combinados = {
    'titulos_artigos': [titulo.get_text() for titulo in titulos],
    'preco_bitcoin': dados_api['bpi']['USD']['rate']
}

with open('dados_combinados.json', 'w') as arquivo:
    json.dump(dados_combinados, arquivo, indent=4)

print("Dados combinados salvos em 'dados_combinados.json'")

______________________


