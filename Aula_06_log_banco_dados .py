usuario,consulta,timestamp
admin,SELECT * FROM clientes,2024-09-17 10:00:00
joao,SELECT * FROM clientes WHERE cpf='12345678900',2024-09-17 10:01:00
maria,DELETE FROM clientes WHERE id=5,2024-09-17 10:05:00
paulo,UPDATE clientes SET saldo=0 WHERE id=10,2024-09-17 10:10:00
joao,INSERT INTO clientes (nome, cpf) VALUES ('Pedro', '98765432100'),2024-09-17 10:15:00
ana,SELECT senha FROM usuarios WHERE id=1,2024-09-17 10:20:00

_________________

import re

# Função para verificar se uma consulta é suspeita
def verificar_consulta_suspeita(usuario, consulta):
    # Regra 1: Consultas à coluna "senha" são proibidas
    if "senha" in consulta:
        return f"Consulta suspeita: Usuário '{usuario}' tentou acessar a coluna 'senha'."

    # Regra 2: Somente o admin pode realizar "SELECT *"
    if "SELECT *" in consulta and usuario != "admin":
        return f"Consulta suspeita: Usuário '{usuario}' realizou um 'SELECT *'."

    # Regra 3: Consultas DELETE ou UPDATE são críticas
    if re.search(r"DELETE|UPDATE", consulta):
        return f"Consulta crítica: Usuário '{usuario}' realizou um {consulta.split()[0]}."

    # Caso a consulta não seja suspeita, retornar None
    return None

# Caminho para o arquivo de log
arquivo_log = 'log_banco_dados.txt'

# Função para ler o log e verificar conformidade
def auditar_log(arquivo):
    with open(arquivo, 'r') as f:
        linhas = f.readlines()

    # Lista para armazenar as consultas suspeitas
    consultas_suspeitas = []

    # Verificar cada linha do log (pular o cabeçalho)
    for linha in linhas[1:]:
        usuario, consulta, timestamp = linha.strip().split(',')

        # Verificar se a consulta é suspeita
        resultado = verificar_consulta_suspeita(usuario, consulta)

        # Se houver resultado, adicionar à lista de suspeitas
        if resultado:
            consultas_suspeitas.append(f"{resultado} - {timestamp}")

    return consultas_suspeitas

# Executar a auditoria do log
consultas_nao_conformes = auditar_log(arquivo_log)

# Exibir os resultados
if consultas_nao_conformes:
    print("Consultas em não conformidade com as regras de auditoria:")
    for consulta in consultas_nao_conformes:
        print(f"- {consulta}")
else:
    print("Todas as consultas estão em conformidade.")

_________________

# Salvando o relatório de consultas não conformes em um arquivo
with open('relatorio_auditoria_banco.txt', 'w') as arquivo_saida:
    if consultas_nao_conformes:
        arquivo_saida.write("Consultas em não conformidade com as regras de auditoria:\n")
        for consulta in consultas_nao_conformes:
            arquivo_saida.write(f"- {consulta}\n")
    else:
        arquivo_saida.write("Todas as consultas estão em conformidade.\n")
