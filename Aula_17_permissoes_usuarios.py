usuario,funcao,recurso,permissao
admin,administrador,clientes,leitura
admin,administrador,clientes,escrita
admin,administrador,financas,leitura
admin,administrador,financas,escrita
joao,funcionario,clientes,leitura
joao,funcionario,clientes,escrita
joao,funcionario,financas,leitura
maria,gerente,clientes,leitura
maria,gerente,clientes,escrita
maria,gerente,financas,leitura

__

import csv

# Função para auditar permissões de usuários com base nas funções
def auditar_permissoes(arquivo_permissoes):
    alertas = []
    permissoes_por_funcao = {
        'administrador': {'clientes': ['leitura', 'escrita'], 'financas': ['leitura', 'escrita']},
        'funcionario': {'clientes': ['leitura'], 'financas': []},
        'gerente': {'clientes': ['leitura', 'escrita'], 'financas': ['leitura']}
    }

    # Ler o arquivo de permissões
    with open(arquivo_permissoes, 'r') as csvfile:
        leitor = csv.DictReader(csvfile)
        for linha in leitor:
            usuario = linha['usuario']
            funcao = linha['funcao']
            recurso = linha['recurso']
            permissao = linha['permissao']

            # Verificar se a função do usuário tem permissão para o recurso e operação
            permissoes_validas = permissoes_por_funcao.get(funcao, {}).get(recurso, [])
            if permissao not in permissoes_validas:
                alertas.append(f"Alerta: Usuário '{usuario}' com função '{funcao}' possui permissão '{permissao}' no recurso '{recurso}', o que é inadequado.")

    return alertas

# Função para exibir alertas
def exibir_alertas(alertas):
    if alertas:
        print("Alertas detectados:")
        for alerta in alertas:
            print(f"- {alerta}")
    else:
        print("Nenhuma permissão inadequada detectada.")

# Executar a auditoria de permissões
arquivo_permissoes = 'permissoes_usuarios.txt'
alertas = auditar_permissoes(arquivo_permissoes)
exibir_alertas(alertas)

__

# Função para salvar alertas em um arquivo
def salvar_alertas_em_arquivo(alertas, arquivo_saida='alertas_permissoes.txt'):
    with open(arquivo_saida, 'w') as f:
        if alertas:
            for alerta in alertas:
                f.write(f"{alerta}\n")
        else:
            f.write("Nenhuma permissão inadequada detectada.\n")

# Salvar os alertas em um arquivo
salvar_alertas_em_arquivo(alertas)

__

