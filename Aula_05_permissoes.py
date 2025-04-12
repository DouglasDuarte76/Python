import os
import stat

def verificar_permissoes(arquivo):
    permissoes = os.stat(arquivo).st_mode
    return {
        'readable': bool(permissoes & stat.S_IRUSR),
        'writable': bool(permissoes & stat.S_IWUSR),
        'executable': bool(permissoes & stat.S_IXUSR)
    }

def modificar_permissoes(arquivo, leitura=None, escrita=None, execucao=None):
    permissoes_atual = os.stat(arquivo).st_mode

    if leitura is not None:
        if leitura:
            permissoes_atual |= stat.S_IRUSR
        else:
            permissoes_atual &= ~stat.S_IRUSR

    if escrita is not None:
        if escrita:
            permissoes_atual |= stat.S_IWUSR
        else:
            permissoes_atual &= ~stat.S_IWUSR

    if execucao is not None:
        if execucao:
            permissoes_atual |= stat.S_IXUSR
        else:
            permissoes_atual &= ~stat.S_IXUSR

    os.chmod(arquivo, permissoes_atual)

# Exemplo de uso
arquivo = input("Digite o caminho do arquivo para verificar permissões: ")

# Verificar permissões atuais
permissoes = verificar_permissoes(arquivo)
print(f"Permissões atuais: Leitura: {permissoes['readable']}, Escrita: {permissoes['writable']}, Execução: {permissoes['executable']}")

# Modificar permissões
modificar = input("Deseja modificar permissões? (s/n): ")
if modificar.lower() == 's':
    leitura = input("Permitir leitura? (s/n): ").lower() == 's'
    escrita = input("Permitir escrita? (s/n): ").lower() == 's'
    execucao = input("Permitir execução? (s/n): ").lower() == 's'

    modificar_permissoes(arquivo, leitura, escrita, execucao)
    print("Permissões modificadas com sucesso!")

# Verificar permissões após modificação
permissoes_modificadas = verificar_permissoes(arquivo)
print(f"Novas permissões: Leitura: {permissoes_modificadas['readable']}, Escrita: {permissoes_modificadas['writable']}, Execução: {permissoes_modificadas['executable']}")
