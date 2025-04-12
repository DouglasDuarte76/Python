2024-09-17 10:00:00 - INFO - Usuário 'joao' consentiu com a coleta de dados.
2024-09-17 10:05:00 - INFO - Dados pessoais coletados para o usuário 'joao'.
2024-09-17 10:10:00 - INFO - Usuário 'maria' consentiu com a coleta de dados.
2024-09-17 10:15:00 - INFO - Usuário 'maria' solicitou a exclusão de seus dados.
2024-09-17 10:20:00 - INFO - Dados pessoais do usuário 'maria' excluídos.
2024-09-17 10:25:00 - INFO - Dados pessoais coletados para o usuário 'pedro'.
2024-09-17 10:30:00 - INFO - Usuário 'pedro' solicitou a exclusão de seus dados.

___

import re

# Função para verificar a conformidade com a LGPD
def verificar_conformidade_lgpd(arquivo_log):
    consentimentos = set()
    solicitacoes_exclusao = set()
    exclusoes_concluidas = set()
    alertas = []

    # Abrir o arquivo de log
    with open(arquivo_log, 'r') as f:
        linhas = f.readlines()

    # Analisar cada linha do log
    for linha in linhas:
        # Verificar consentimentos
        match_consentimento = re.search(r"Usuário '(\w+)' consentiu com a coleta de dados", linha)
        if match_consentimento:
            usuario = match_consentimento.group(1)
            consentimentos.add(usuario)

        # Verificar coleta de dados
        match_coleta = re.search(r"Dados pessoais coletados para o usuário '(\w+)'", linha)
        if match_coleta:
            usuario = match_coleta.group(1)
            if usuario not in consentimentos:
                alertas.append(f"Alerta: Coleta de dados sem consentimento para o usuário '{usuario}'")

        # Verificar solicitações de exclusão
        match_solicitacao_exclusao = re.search(r"Usuário '(\w+)' solicitou a exclusão de seus dados", linha)
        if match_solicitacao_exclusao:
            usuario = match_solicitacao_exclusao.group(1)
            solicitacoes_exclusao.add(usuario)

        # Verificar exclusão de dados
        match_exclusao = re.search(r"Dados pessoais do usuário '(\w+)' excluídos", linha)
        if match_exclusao:
            usuario = match_exclusao.group(1)
            exclusoes_concluidas.add(usuario)

    # Verificar se todas as solicitações de exclusão foram atendidas
    for usuario in solicitacoes_exclusao:
        if usuario not in exclusoes_concluidas:
            alertas.append(f"Alerta: Solicitação de exclusão não atendida para o usuário '{usuario}'")

    return alertas

# Caminho para o arquivo de log de conformidade
arquivo_log = 'log_conformidade.txt'

# Executar a verificação de conformidade com a LGPD
alertas_conformidade = verificar_conformidade_lgpd(arquivo_log)

# Exibir os alertas de conformidade
if alertas_conformidade:
    print("Alertas de não conformidade com a LGPD detectados:")
    for alerta in alertas_conformidade:
        print(f"- {alerta}")
else:
    print("Todos os registros estão em conformidade com a LGPD.")

___

# Função para salvar os alertas de conformidade em um arquivo
def salvar_alertas(alertas, arquivo_saida='alertas_conformidade_lgpd.txt'):
    with open(arquivo_saida, '
