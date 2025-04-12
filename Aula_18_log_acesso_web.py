192.168.1.10 - - [17/Sep/2024:10:00:00 +0000] "GET /login HTTP/1.1" 200 4523
192.168.1.10 - - [17/Sep/2024:10:01:00 +0000] "POST /login HTTP/1.1" 401 234
192.168.1.10 - - [17/Sep/2024:10:02:00 +0000] "POST /login HTTP/1.1" 401 234
192.168.1.10 - - [17/Sep/2024:10:03:00 +0000] "POST /login HTTP/1.1" 401 234
192.168.1.15 - - [17/Sep/2024:10:05:00 +0000] "GET /admin HTTP/1.1" 403 298
192.168.1.15 - - [17/Sep/2024:10:06:00 +0000] "GET /config HTTP/1.1" 404 143
192.168.1.20 - - [17/Sep/2024:10:10:00 +0000] "GET /index.html HTTP/1.1" 200 5231
192.168.1.10 - - [17/Sep/2024:10:12:00 +0000] "POST /login HTTP/1.1" 200 4523
192.168.1.10 - - [17/Sep/2024:10:15:00 +0000] "GET /admin HTTP/1.1" 403 298
192.168.1.15 - - [17/Sep/2024:10:20:00 +0000] "GET /nonexistent HTTP/1.1" 404 143

___


import re

# Função para auditar logs de acesso web
def auditar_logs_web(arquivo_log):
    alertas = []
    tentativas_login = {}
    
    with open(arquivo_log, 'r') as f:
        linhas = f.readlines()

    # Verificar cada linha do log
    for linha in linhas:
        # Padrão de log
        match_log = re.search(r"(\d{3}\.\d{3}\.\d{1}\.\d{1,3}) - - \[\S+ \+\d+\] \"(\w+) (\S+) HTTP/\d\.\d\" (\d{3})", linha)
        if match_log:
            ip = match_log.group(1)
            metodo_http = match_log.group(2)
            url = match_log.group(3)
            status = int(match_log.group(4))

            # Verificar tentativas de login (401 falhas e 200 sucesso)
            if "/login" in url:
                if ip not in tentativas_login:
                    tentativas_login[ip] = {"falhas": 0, "sucesso": False}

                if status == 401:
                    tentativas_login[ip]["falhas"] += 1
                elif status == 200:
                    tentativas_login[ip]["sucesso"] = True

                # Se houver 3 falhas seguidas de um sucesso, gerar alerta
                if tentativas_login[ip]["falhas"] >= 3 and tentativas_login[ip]["sucesso"]:
                    alertas.append(f"Alerta: Tentativa de força bruta no login detectada do IP {ip} - {linha.strip()}")
                    tentativas_login[ip] = {"falhas": 0, "sucesso": False}  # Resetar

            # Verificar tentativas de acessar URLs sensíveis
            if url in ["/admin", "/config"]:
                if status == 403 or status == 404:
                    alertas.append(f"Alerta: Tentativa de acesso não autorizado a '{url}' do IP {ip} - {linha.strip()}")

            # Verificar acessos a URLs inexistentes
            if status == 404:
                alertas.append(f"Alerta: Tentativa de acesso a URL inexistente '{url}' do IP {ip} - {linha.strip()}")

    return alertas

# Função para exibir alertas
def exibir_alertas(alertas):
    if alertas:
        print("Alertas detectados:")
        for alerta in alertas:
            print(f"- {alerta}")
    else:
        print("Nenhuma atividade suspeita detectada.")

# Executar a auditoria de logs web
arquivo_log = 'log_acesso_web.txt'
alertas = auditar_logs_web(arquivo_log)
exibir_alertas(alertas)

___

# Função para salvar alertas em um arquivo
def salvar_alertas_em_arquivo(alertas, arquivo_saida='alertas_web.txt'):
    with open(arquivo_saida, 'a') as f:
        if alertas:
            for alerta in alertas:
                f.write(f"{alerta}\n")
        else:
            f.write("Nenhuma atividade suspeita detectada.\n")

# Salvar os alertas em um arquivo
salvar_alertas_em_arquivo(alertas)

___

