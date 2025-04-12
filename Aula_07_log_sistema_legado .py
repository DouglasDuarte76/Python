2024-09-17 09:00:00 - INFO - Usuário 'admin' logou no sistema.
2024-09-17 09:05:00 - ERROR - Tentativa de login falhou para o usuário 'joao'.
2024-09-17 09:10:00 - WARNING - Tentativa de login falhou para o usuário 'joao'.
2024-09-17 09:15:00 - ERROR - Tentativa de login falhou para o usuário 'maria'.
2024-09-17 09:20:00 - INFO - Usuário 'maria' logou no sistema.
2024-09-17 09:25:00 - ERROR - Tentativa de login falhou para o usuário 'joao'.
2024-09-17 09:30:00 - INFO - Usuário 'ana' logou no sistema.

_________________


import re
from collections import defaultdict

# Função para monitorar o log do sistema legado
def monitorar_logs(arquivo_log):
    # Dicionário para contar tentativas de login falhadas por usuário
    falhas_login = defaultdict(int)
    
    # Lista de alertas gerados
    alertas = []

    # Abrir o arquivo de log para leitura
    with open(arquivo_log, 'r') as f:
        linhas = f.readlines()

    # Verificar cada linha do log
    for linha in linhas:
        # Verificar tentativas de login falhadas
        match_falha = re.search(r"Tentativa de login falhou para o usuário '(\w+)'", linha)
        if match_falha:
            usuario = match_falha.group(1)
            falhas_login[usuario] += 1
            
            # Verificar se houve 3 falhas consecutivas
            if falhas_login[usuario] >= 3:
                alertas.append(f"Alerta: Possível ataque de força bruta no usuário '{usuario}' - {linha.strip()}")
        else:
            # Se o usuário logou com sucesso, resetar o contador de falhas
            match_login = re.search(r"Usuário '(\w+)' logou no sistema", linha)
            if match_login:
                usuario = match_login.group(1)
                falhas_login[usuario] = 0

    return alertas

# Caminho para o arquivo de log do sistema legado
arquivo_log = 'log_sistema_legado.txt'

# Executar o monitoramento dos logs
alertas_detectados = monitorar_logs(arquivo_log)

# Exibir os alertas
if alertas_detectados:
    print("Alertas de atividades suspeitas:")
    for alerta in alertas_detectados:
        print(f"- {alerta}")
else:
    print("Nenhuma atividade suspeita detectada.")


_________________

# Salvando os alertas de atividades suspeitas em um arquivo
with open('alertas_atividades_suspeitas.txt', 'w') as arquivo_saida:
    if alertas_detectados:
        arquivo_saida.write("Alertas de atividades suspeitas:\n")
        for alerta in alertas_detectados:
            arquivo_saida.write(f"- {alerta}\n")
    else:
        arquivo_saida.write("Nenhuma atividade suspeita detectada.\n")


