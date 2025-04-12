[2024-09-17 10:00:00] INFO: Tentativa de login do usuário 'joao'.
[2024-09-17 10:01:00] ERROR: Senha incorreta para o usuário 'joao'.
[2024-09-17 10:02:00] INFO: Tentativa de login do usuário 'maria'.
[2024-09-17 10:03:00] INFO: Login bem-sucedido para o usuário 'maria'.
[2024-09-17 10:05:00] INFO: Tentativa de login do usuário 'joao'.
[2024-09-17 10:06:00] ERROR: Senha incorreta para o usuário 'joao'.
[2024-09-17 10:07:00] ERROR: Senha incorreta para o usuário 'joao'.
[2024-09-17 10:08:00] INFO: Tentativa de login do usuário 'joao'.


_____________________________________________________________________________

import re

# Definir o limite de falhas consecutivas antes de acionar o alarme
LIMITE_FALHAS = 3

# Caminho para o arquivo de log
caminho_log = 'auth.log'

# Dicionário para contar as falhas de login consecutivas
falhas_consecutivas = {}

# Expressão regular para capturar tentativas de login e falhas
padrao_falha = r"ERROR: Senha incorreta para o usuário '(\w+)'"
padrao_login = r"INFO: Tentativa de login do usuário '(\w+)'"

with open(caminho_log, 'r') as arquivo:
    linhas = arquivo.readlines()

# Analisar o log
for linha in linhas:
    # Verificar tentativas de login
    match_login = re.search(padrao_login, linha)
    if match_login:
        usuario = match_login.group(1)
        # Reseta o contador de falhas se houver uma nova tentativa de login
        if usuario in falhas_consecutivas:
            falhas_consecutivas[usuario] = 0

    # Verificar falhas de autenticação
    match_falha = re.search(padrao_falha, linha)
    if match_falha:
        usuario = match_falha.group(1)
        if usuario in falhas_consecutivas:
            falhas_consecutivas[usuario] += 1
        else:
            falhas_consecutivas[usuario] = 1

        # Verificar se o número de falhas consecutivas ultrapassou o limite
        if falhas_consecutivas[usuario] >= LIMITE_FALHAS:
            print(f"Alerta: Múltiplas falhas consecutivas para o usuário '{usuario}'")

_____________________________________________________________________________

with open('alertas.log', 'w') as arquivo_alertas:
    for linha in linhas:
        match_falha = re.search(padrao_falha, linha)
        if match_falha:
            usuario = match_falha.group(1)
            if usuario in falhas_consecutivas:
                falhas_consecutivas[usuario] += 1
            else:
                falhas_consecutivas[usuario] = 1

            if falhas_consecutivas[usuario] >= LIMITE_FALHAS:
                arquivo_alertas.write(f"Alerta: Múltiplas falhas consecutivas para o usuário '{usuario}'\n")

_____________________________________________________________________________
