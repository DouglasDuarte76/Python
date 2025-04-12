servico-carrinho -> servico-pagamento [POST /api/pagamento] - Token: abc123 - Status: 200
servico-usuario -> servico-relatorio [GET /api/relatorio] - Token: xyz789 - Status: 200
servico-relatorio -> servico-pagamento [GET /api/pagamento/status] - Token: - - Status: 401
servico-carrinho -> servico-pagamento [POST /api/pagamento] - Token: abc123 - Status: 403
servico-usuario -> servico-pagamento [GET /api/pagamento/historico] - Token: lmn456 - Status: 200
servico-relatorio -> servico-pagamento [GET /api/pagamento/status] - Token: - - Status: 403


___


import re

# Função para auditar logs de microserviços
def auditar_logs_microservicos(arquivo_log):
    alertas = []
    
    with open(arquivo_log, 'r') as f:
        linhas = f.readlines()

    # Verificar cada linha do log
    for linha in linhas:
        match_log = re.search(r"(\S+) -> (\S+) \[\S+ (\S+)\] - Token: (\S+) - Status: (\d{3})", linha)
        if match_log:
            servico_origem = match_log.group(1)
            servico_destino = match_log.group(2)
            endpoint = match_log.group(3)
            token = match_log.group(4)
            status = int(match_log.group(5))

            # Verificar requisições sem token de autenticação
            if token == '-' and status == 401:
                alertas.append(f"Alerta: Requisição não autenticada do serviço '{servico_origem}' para o serviço '{servico_destino}' no endpoint '{endpoint}'")

            # Verificar requisições com status 403 (acesso não autorizado)
            if status == 403:
                alertas.append(f"Alerta: Tentativa de acesso não autorizado do serviço '{servico_origem}' ao serviço '{servico_destino}' no endpoint '{endpoint}'")

    return alertas

# Função para exibir alertas
def exibir_alertas(alertas):
    if alertas:
        print("Alertas detectados:")
        for alerta in alertas:
            print(f"- {alerta}")
    else:
        print("Nenhuma atividade suspeita detectada.")

# Executar a auditoria de logs de microserviços
arquivo_log = 'log_microservicos.txt'
alertas = auditar_logs_microservicos(arquivo_log)
exibir_alertas(alertas)

___
# Função para salvar alertas em um arquivo
def salvar_alertas_em_arquivo(alertas, arquivo_saida='alertas_microservicos.txt'):
    with open(arquivo_saida, 'w') as f:
        if alertas:
            for alerta in alertas:
                f.write(f"{alerta}\n")
        else:
            f.write("Nenhuma atividade suspeita detectada.\n")

# Salvar os alertas em um arquivo
salvar_alertas_em_arquivo(alertas)

___

