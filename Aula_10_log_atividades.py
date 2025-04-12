2024-09-17 10:00:00 - INFO - Usuário 'admin' acessou os registros de clientes.
2024-09-17 10:05:00 - INFO - Usuário 'joao' tentou acessar a coluna 'senha' na tabela 'usuarios'.
2024-09-17 10:10:00 - WARNING - Usuário 'maria' apagou o log de auditoria.
2024-09-17 10:15:00 - INFO - Usuário 'admin' acessou a tabela 'pagamentos'.
2024-09-17 10:20:00 - INFO - Usuário 'ana' consultou dados sensíveis na tabela 'usuarios'.

____

import re

# Função para analisar o log e identificar comportamento antiético
def analisar_log_eticamente(arquivo_log):
    alertas = []
    
    # Abrir o arquivo de log para leitura
    with open(arquivo_log, 'r') as f:
        linhas = f.readlines()
    
    # Verificar cada linha do log
    for linha in linhas:
        # Regra 1: Tentativa de acessar a coluna 'senha'
        if re.search(r"acessar a coluna 'senha'", linha):
            alertas.append(f"Alerta Ético: Tentativa de acessar a coluna 'senha'. - {linha.strip()}")
        
        # Regra 2: Apagar ou manipular logs
        if re.search(r"apagou o log|manipulou o log", linha):
            alertas.append(f"Alerta Ético: Tentativa de apagar ou manipular logs. - {linha.strip()}")
    
    return alertas

# Caminho para o arquivo de log
arquivo_log = 'log_atividades.txt'

# Executar a análise ética do log
alertas_eticamente_suspeitos = analisar_log_eticamente(arquivo_log)

# Exibir os alertas de comportamento antiético
if alertas_eticamente_suspeitos:
    print("Alertas de comportamento antiético detectados:")
    for alerta in alertas_eticamente_suspeitos:
        print(f"- {alerta}")
else:
    print("Nenhum comportamento antiético detectado.")


____

# Função para salvar os alertas de comportamento antiético em um arquivo
def salvar_alertas(alertas, arquivo_saida='alertas_eticamente_suspeitos.txt'):
    with open(arquivo_saida, 'w') as f:
        if alertas:
            f.write("Alertas de comportamento antiético detectados:\n")
            for alerta in alertas:
                f.write(f"{alerta}\n")
        else:
            f.write("Nenhum comportamento antiético detectado.\n")

# Salvar os alertas em um arquivo
salvar_alertas(alertas_eticamente_suspeitos)


____

