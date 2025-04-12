[2024-09-17 12:00:00] INFO: Sistema iniciado.
[2024-09-17 12:01:00] ERROR: Falha ao acessar o banco de dados.
[2024-09-17 12:02:00] WARNING: Tempo de resposta lento.
[2024-09-17 12:03:00] INFO: Conexão com o banco de dados restabelecida.
[2024-09-17 12:05:00] ERROR: Falha na autenticação do usuário.

___________________________________________________________________________________________

import re

# Caminho para o arquivo de log
caminho_log = 'sistema.log'

# Expressão regular para capturar linhas com ERROR ou WARNING
padrao_erro = r"(ERROR|WARNING):.*"

# Abrir e ler o arquivo de log
with open(caminho_log, 'r') as arquivo:
    linhas = arquivo.readlines()

# Analisar o log em busca de erros e alertas
for linha in linhas:
    if re.search(padrao_erro, linha):
        print(f"Aviso ou Erro encontrado: {linha.strip()}")

___________________________________________________________________________________________

with open('resultados_auditoria.txt', 'w') as arquivo_saida:
    for linha in linhas:
        if re.search(padrao_erro, linha):
            arquivo_saida.write(f"Aviso ou Erro encontrado: {linha.strip()}\n")
