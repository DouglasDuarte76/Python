import requests
from bs4 import BeautifulSoup

# Função para detectar vulnerabilidade de injeção de SQL
def verificar_injecao_sql(url):
    payload = "' OR '1'='1"
    response = requests.get(url, params={"id": payload})
    if "mysql" in response.text.lower() or "syntax" in response.text.lower():
        print(f"[+] Possível vulnerabilidade de Injeção de SQL detectada em {url}")
    else:
        print(f"[-] Nenhuma vulnerabilidade de Injeção de SQL detectada em {url}")

# Função para detectar vulnerabilidade de XSS
def verificar_xss(url):
    payload = "<script>alert('XSS')</script>"
    response = requests.get(url, params={"q": payload})
    soup = BeautifulSoup(response.text, "html.parser")
    if payload in soup.prettify():
        print(f"[+] Possível vulnerabilidade de XSS detectada em {url}")
    else:
        print(f"[-] Nenhuma vulnerabilidade de XSS detectada em {url}")

# URL alvo
url_alvo = input("Digite a URL da aplicação web para análise: ")

# Executar verificações de vulnerabilidades
verificar_injecao_sql(url_alvo)
verificar_xss(url_alvo)
