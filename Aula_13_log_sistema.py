2024-09-17 10:00:00 - INFO - Usuário 'admin' logou no sistema.
2024-09-17 10:05:00 - ERROR - Tentativa de login falhou para o usuário 'joao'.
2024-09-17 10:06:00 - ERROR - Tentativa de login falhou para o usuário 'joao'.
2024-09-17 10:07:00 - ERROR - Tentativa de login falhou para o usuário 'joao'.
2024-09-17 10:08:00 - WARNING - Usuário 'maria' acessou o recurso 'dados_sensíveis'.
2024-09-17 10:10:00 - INFO - Usuário 'admin' acessou o recurso 'pagamentos'.

___


import re
import time
from collections import defaultdict

# Função para monitorar os logs em tempo real
def monitorar_logs(arquivo_log):
    falhas_login = defaultdict(int)
    alertas = []

    with open(arquivo_log, 'r') as f:
        linhas = f.readlines()

    # Processar cada linha do log
    for linha in linhas:
        # Verificar tentativas de login falhadas
        match_falha_login = re.search(r"Tentativa de login falhou para o usuário '(\w+)'", linha)
        if match_falha_login:
            usuario = match_falha_login.group(1)
            falhas_login[usuario] += 1
            if falhas_login[usuario] >= 3:
                alertas.append(f"Alerta: Tentativas de login falhadas consecutivas para o usuário '{usuario}' - {linha.strip()}")
        else:
            # Resetar o contador de falhas após um login bem-sucedido ou outras ações
            falhas_login.clear()

        # Verificar acessos a recursos sensíveis
        match_acesso_sensivel = re.search(r"Usuário '(\w+)' acessou o recurso 'dados_sensíveis'", linha)
        if match_acesso_sensivel:
            usuario = match_acesso_sensivel.group(1)
            if usuario != 'admin':
                alertas.append(f"Alerta: Acesso não autorizado ao recurso 'dados_sensíveis' pelo usuário '{usuario}' - {linha.strip()}")

    return alertas

# Função principal para monitorar em tempo real (simulação)
def monitorar_em_tempo_real(arquivo_log, intervalo=5):
    print("Monitorando logs em tempo real...")
    while True:
        alertas = monitorar_logs(arquivo_log)
        if alertas:
            print("Alertas detectados:")
            for alerta in alertas:
                print(f"- {alerta}")
        else:
            print("Nenhuma atividade suspeita detectada.")
        time.sleep(intervalo)

# Simulação de monitoramento em tempo real
monitorar_em_tempo_real('log_sistema.txt')

____



# Função para salvar alertas em um arquivo
def salvar_alertas_em_arquivo(alertas, arquivo_saida='alertas_monitoramento.txt'):
    with open(arquivo_saida, 'a') as f:
        if alertas:
            for alerta in alertas:
                f.write(f"{alerta}\n")

# Modificar o monitoramento para salvar alertas em um arquivo
def monitorar_em_tempo_real_com_arquivo(arquivo_log, intervalo=5):
    print("Monitorando logs e salvando alertas em tempo real...")
    while True:
        alertas = monitorar_logs(arquivo_log)
        if alertas:
            print("Alertas detectados, salvando em arquivo...")
            salvar_alertas_em_arquivo(alertas)
        else:
            print("Nenhuma atividade suspeita detectada.")
        time.sleep(intervalo)

# Executar o monitoramento com salvamento em arquivo
monitorar_em_tempo_real_com_arquivo('log_sistema.txt')

____


