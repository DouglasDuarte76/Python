192.168.1.10 - - [17/Sep/2024:10:00:00 +0000] "GET /api/user/profile HTTP/1.1" 200 - Token: abc123
192.168.1.11 - - [17/Sep/2024:10:02:00 +0000] "GET /api/admin/dashboard HTTP/1.1" 403 - Token: xyz789
192.168.1.10 - - [17/Sep/2024:10:05:00 +0000] "POST /api/user/update HTTP/1.1" 200 - Token: abc123
192.168.1.12 - - [17/Sep/2024:10:10:00 +0000] "DELETE /api/user/delete HTTP/1.1" 401 - Token: -
192.168.1.10 - - [17/Sep/2024:10:12:00 +0000] "GET /api/admin/settings HTTP/1.1" 403 - Token: abc123
192.168.1.13 - - [17/Sep/2024:10:15:00 +0000] "POST /api/user/create HTTP/1.1" 200 - Token: lmn456
192.168.1.11 - - [17/Sep/2024:10:18:00 +0000] "GET /api/admin/users HTTP/1.1" 403 - Token: xyz789

___


import re

# Função para auditar logs de API
def auditar_logs_api(arquivo_log):
    alertas = []
    
    with open(arquivo_log, 'r') as f:
        linhas = f.readlines()

    # Verificar cada linha do log
    for linha in linhas:
        # Padrão de log
        match_log = re.search(r"(\d{3}\.\d{3}\.\d{1}\.\d{1,3}) - - \[\S+ \+\d+\] \"(\w+) (\S+) HTTP/\d\.\d\" (\d{3}) - Token: (\S+)", linha)
        if match_log:
            ip = match_log.group(1)
            metodo_http = match_log.group(2)
            url = match_log.group(3)
            status = int(match_log.group(4))
            token = match_log.group(5)

            # Verificar endpoints administrativos sem token válido
            if "/api/admin/" in url and (token == '-' or status == 403):
                alertas.append(f"Alerta: Tentativa de acesso não autorizado ao endpoint '{url}' pelo IP {ip} - Status {status}")

            # Verificar requisições sem token de autenticação
            if token == '-' and status == 401:
                alertas.append(f"Alerta: Requisição não autenticada ao endpoint '{url}' pelo IP {ip}")

    return alertas

# Função para exibir alertas
def exibir_alertas(alertas):
    if alertas:
        print("Alertas detectados:")
        for alerta in alertas:
            print(f"- {alerta}")
    else:
        print("Nenhuma atividade suspeita detectada.")

# Executar a auditoria de logs de API
arquivo_log = 'log_api.txt'
alertas = auditar_logs_api(arquivo_log)
exibir_alertas(alertas)

____


# Função para salvar alertas em um arquivo
def salvar_alertas_em_arquivo(alertas, arquivo_saida='alertas_api.txt'):
    with open(arquivo_saida, 'a') as f:
        if alertas:
            for alerta in alertas:
                f.write(f"{alerta}\n")
        else:
            f.write("Nenhuma atividade suspeita detectada.\n")

# Salvar os alertas em um arquivo
salvar_alertas_em_arquivo(alertas)

