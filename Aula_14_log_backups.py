2024-09-17 01:00:00 - INFO - Backup iniciado.
2024-09-17 01:05:00 - INFO - Backup concluído com sucesso.
2024-09-17 03:00:00 - INFO - Backup iniciado.
2024-09-17 03:05:00 - ERROR - Falha ao realizar o backup.
2024-09-17 05:00:00 - INFO - Backup iniciado.
2024-09-17 05:05:00 - INFO - Backup concluído com sucesso.
2024-09-17 07:00:00 - INFO - Backup iniciado.
2024-09-17 07:10:00 - INFO - Backup concluído com sucesso.

__


import re
from datetime import datetime, timedelta

# Função para monitorar e auditar os logs de backup
def auditar_backups(arquivo_log):
    alertas = []
    ultima_execucao = None
    intervalo_esperado = timedelta(hours=2)

    with open(arquivo_log, 'r') as f:
        linhas = f.readlines()

    # Verificar cada linha do log
    for linha in linhas:
        # Verificar se o backup foi iniciado
        match_backup_inicio = re.search(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - INFO - Backup iniciado", linha)
        if match_backup_inicio:
            timestamp = match_backup_inicio.group(1)
            data_backup_inicio = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
            
            # Verificar se o backup está dentro do intervalo esperado
            if ultima_execucao and (data_backup_inicio - ultima_execucao) > intervalo_esperado:
                alertas.append(f"Alerta: Atraso na execução do backup. Último backup em {ultima_execucao.strftime('%Y-%m-%d %H:%M:%S')}.")
            
            ultima_execucao = data_backup_inicio

        # Verificar se o backup foi concluído com sucesso
        match_backup_sucesso = re.search(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - INFO - Backup concluído com sucesso", linha)
        if match_backup_sucesso:
            continue

        # Verificar se houve falha no backup
        match_backup_falha = re.search(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - ERROR - Falha ao realizar o backup", linha)
        if match_backup_falha:
            timestamp = match_backup_falha.group(1)
            alertas.append(f"Alerta: Falha no backup em {timestamp}.")

    return alertas

# Função para exibir alertas
def exibir_alertas(alertas):
    if alertas:
        print("Alertas detectados:")
        for alerta in alertas:
            print(f"- {alerta}")
    else:
        print("Nenhum alerta. Todos os backups foram executados corretamente.")

# Executar a auditoria de backups
arquivo_log = 'log_backups.txt'
alertas = auditar_backups(arquivo_log)
exibir_alertas(alertas)

___


# Função para salvar alertas em um arquivo
def salvar_alertas_em_arquivo(alertas, arquivo_saida='alertas_backups.txt'):
    with open(arquivo_saida, 'a') as f:
        if alertas:
            for alerta in alertas:
                f.write(f"{alerta}\n")
        else:
            f.write("Nenhum alerta. Todos os backups foram executados corretamente.\n")

# Modificar o monitoramento para salvar alertas em um arquivo
alertas = auditar_backups(arquivo_log)
salvar_alertas_em_arquivo(alertas)

