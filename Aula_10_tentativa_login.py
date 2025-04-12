import re

# Função para analisar logs de autenticação
def analisar_logs(caminho_log):
    try:
        with open(caminho_log, 'r') as log_file:
            for linha in log_file:
                # Procurar por tentativas de login falhas
                if "Failed password" in linha:
                    # Extrair e exibir informações relevantes
                    timestamp = linha.split()[0:3]
                    ip_origem = re.search(r'[0-9]+(?:\.[0-9]+){3}', linha)
                    user = re.search(r'for\s(\w+)\sfrom', linha)
                    print(f"[Tentativa de Login Falha] Data: {' '.join(timestamp)}, Usuário: {user.group(1) if user else 'Desconhecido'}, IP de Origem: {ip_origem.group(0) if ip_origem else 'Desconhecido'}")
    except FileNotFoundError:
        print(f"Arquivo de log não encontrado: {caminho_log}")
    except Exception as e:
        print(f"Erro ao analisar o log: {e}")

# Caminho para o arquivo de log de autenticação
caminho_log = "/var/log/auth.log"

# Executar análise de logs
analisar_logs(caminho_log)
