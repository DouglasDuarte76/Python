usuario,permissao
admin,admin
joao,regular
maria,regular
paulo,admin
ana,regular
carlos,admin
jose,regular

__________________________________________________

# Caminho para o arquivo de usuários e permissões
arquivo_permissoes = 'usuarios_permissoes.txt'

# Função para verificar conformidade
def verificar_conformidade(arquivo):
    # Abrir o arquivo e ler as permissões
    with open(arquivo, 'r') as f:
        linhas = f.readlines()

    # Lista de usuários em não conformidade
    nao_conformes = []

    # Verificar cada linha do arquivo
    for linha in linhas[1:]:  # Pular o cabeçalho
        usuario, permissao = linha.strip().split(',')
        
        # Verificar se um usuário regular tem permissões de admin
        if permissao == 'admin' and usuario != 'admin':
            nao_conformes.append(usuario)

    return nao_conformes

# Executar a verificação e gerar o relatório
usuarios_nao_conformes = verificar_conformidade(arquivo_permissoes)

# Exibir os resultados
if usuarios_nao_conformes:
    print("Usuários em não conformidade com as permissões:")
    for usuario in usuarios_nao_conformes:
        print(f"- {usuario}")
else:
    print("Todos os usuários estão em conformidade.")

__________________________________________________

# Salvando o relatório de não conformidade em um arquivo
with open('relatorio_auditoria.txt', 'w') as arquivo_saida:
    if usuarios_nao_conformes:
        arquivo_saida.write("Usuários em não conformidade com as permissões:\n")
        for usuario in usuarios_nao_conformes:
            arquivo_saida.write(f"- {usuario}\n")
    else:
        arquivo_saida.write("Todos os usuários estão em conformidade.\n")
