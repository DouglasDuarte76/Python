2024-09-17 09:00:00 - INFO - Usuário 'admin' executou SELECT * FROM clientes.
2024-09-17 09:10:00 - INFO - Usuário 'joao' executou UPDATE clientes SET saldo=0 WHERE id=5.
2024-09-17 09:15:00 - WARNING - Usuário 'joao' tentou acessar a tabela 'pagamentos'.
2024-09-17 09:20:00 - INFO - Usuário 'admin' executou DELETE FROM clientes WHERE id=10.
2024-09-17 09:30:00 - INFO - Usuário 'maria' executou SELECT * FROM produtos.
2024-09-17 09:45:00 - WARNING - Usuário 'joao' tentou alterar a tabela 'usuarios'.

___


import re

# Função para auditar logs de banco de dados
def auditar_banco_dados(arquivo_log):
    alertas = []

    # Abrir o arquivo de log para leitura
    with open(arquivo_log, 'r') as f:
        linhas = f.readlines()

    # Verificar cada linha do log
    for linha in linhas:
        # Verificar se houve tentativa de acesso à tabela 'pagamentos' por alguém que não seja 'admin'
        match_pagamentos = re.search(r"Usuário '(\w+)' tentou acessar a tabela 'pagamentos'", linha)
        if match_pagamentos:
            usuario = match_pagamentos.group(1)
            if usuario != 'admin':
                alertas.append(f"Alerta: Acesso não autorizado à tabela 'pagamentos' pelo usuário '{usuario}' - {linha.strip()}")

        # Verificar se houve tentativa de alterar a tabela 'usuarios' por alguém que não seja 'admin'
        match_alteracao_usuarios = re.search(r"Usuário '(\w+)' tentou alterar a tabela 'usuarios'", linha)
        if match_alteracao_usuarios:
            usuario = match_alteracao_usuarios.group(1)
            if usuario != 'admin':
                alertas.append(f"Alerta: Tentativa de alteração não autorizada na tabela 'usuarios' pelo usuário '{usuario}' - {linha.strip()}")

        # Verificar todas as consultas UPDATE ou DELETE
        match_update_delete = re.search(r"Usuário '(\w+)' executou (UPDATE|DELETE)", linha)
        if match_update_delete:
            usuario = match_update_delete.group(1)
            operacao = match_update_delete.group(2)
            alertas.append(f"Registro de {operacao}: Usuário '{usuario}' executou {operacao} - {linha.strip()}")

    return alertas

# Função para exibir alertas
def exibir_alertas(alertas):
    if alertas:
        print("Alertas detectados:")
        for alerta in alertas:
            print(f"- {alerta}")
    else:
        print("Nenhuma atividade suspeita detectada.")

# Executar a auditoria de banco de dados
arquivo_log = 'log_banco_dados.txt'
alertas = auditar_banco_dados(arquivo_log)
exibir_alertas(alertas)


___


# Função para salvar alertas em um arquivo
def salvar_alertas_em_arquivo(alertas, arquivo_saida='alertas_banco_dados.txt'):
    with open(arquivo_saida, 'a') as f:
        if alertas:
            for alerta in alertas:
                f.write(f"{alerta}\n")
        else:
            f.write("Nenhuma atividade suspeita detectada.\n")

# Salvar os alertas em um arquivo
salvar_alertas_em_arquivo(alertas)


