nome,cpf,email
João Silva,12345678900,joao.silva@example.com
Maria Oliveira,09876543210,maria.oliveira@example.com
Paulo Souza,11122233344,paulo.souza@example.com
Ana Santos,99988877766,ana.santos@example.com

_________________________________________________________

import re

# Função para verificar se o CPF está mascarado
def verificar_cpf_mascarado(cpf):
    # CPF deve ter os 7 primeiros dígitos ocultos, por exemplo: '*******8900'
    return bool(re.match(r"\*{7}\d{4}", cpf))

# Função para verificar se o e-mail está criptografado (simulação)
def verificar_email_criptografado(email):
    # Simular que um e-mail criptografado está em formato embaralhado (para fins de exemplo)
    return email.startswith("ENC(") and email.endswith(")")

# Caminho para o arquivo de dados de usuários
arquivo_dados = 'dados_usuarios.txt'

# Função para verificar conformidade
def verificar_conformidade(arquivo):
    with open(arquivo, 'r') as f:
        linhas = f.readlines()

    # Lista para armazenar os usuários em não conformidade
    nao_conformes = []

    # Verificar cada linha do arquivo (pular o cabeçalho)
    for linha in linhas[1:]:
        nome, cpf, email = linha.strip().split(',')

        # Verificar se o CPF está mascarado
        if not verificar_cpf_mascarado(cpf):
            nao_conformes.append(f"{nome} - CPF não está mascarado corretamente")

        # Verificar se o e-mail está criptografado
        if not verificar_email_criptografado(email):
            nao_conformes.append(f"{nome} - E-mail não está criptografado")

    return nao_conformes

# Executar a verificação e gerar o relatório
usuarios_nao_conformes = verificar_conformidade(arquivo_dados)

# Exibir os resultados
if usuarios_nao_conformes:
    print("Usuários em não conformidade com a proteção de dados:")
    for usuario in usuarios_nao_conformes:
        print(f"- {usuario}")
else:
    print("Todos os usuários estão em conformidade com a proteção de dados.")


_________________________________________________________

# Salvando o relatório de não conformidade em um arquivo
with open('relatorio_conformidade.txt', 'w') as arquivo_saida:
    if usuarios_nao_conformes:
        arquivo_saida.write("Usuários em não conformidade com a proteção de dados:\n")
        for usuario in usuarios_nao_conformes:
            arquivo_saida.write(f"- {usuario}\n")
    else:
        arquivo_saida.write("Todos os usuários estão em conformidade com a proteção de dados.\n")
