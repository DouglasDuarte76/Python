import os  # Importa o módulo 'os', que permite interagir com o sistema operacional, incluindo operações com arquivos e diretórios.
import stat  # Importa o módulo 'stat', que contém constantes para acessar e modificar permissões de arquivos.

# Função para verificar as permissões de um arquivo
def verificar_permissoes(arquivo):
    permissoes = os.stat(arquivo).st_mode  # Usa os.stat() para obter o modo de permissões do arquivo.
    return {
        'readable': bool(permissoes & stat.S_IRUSR),  # Verifica se o arquivo tem permissão de leitura para o usuário.
        'writable': bool(permissoes & stat.S_IWUSR),  # Verifica se o arquivo tem permissão de escrita para o usuário.
        'executable': bool(permissoes & stat.S_IXUSR)  # Verifica se o arquivo tem permissão de execução para o usuário.
    }

# Função para modificar as permissões de um arquivo
def modificar_permissoes(arquivo, leitura=None, escrita=None, execucao=None):
    permissoes_atual = os.stat(arquivo).st_mode  # Obtém as permissões atuais do arquivo.

    # Modifica a permissão de leitura, se especificada.
    if leitura is not None:
        if leitura:
            permissoes_atual |= stat.S_IRUSR  # Adiciona a permissão de leitura.
        else:
            permissoes_atual &= ~stat.S_IRUSR  # Remove a permissão de leitura.

    # Modifica a permissão de escrita, se especificada.
    if escrita is not None:
        if escrita:
            permissoes_atual |= stat.S_IWUSR  # Adiciona a permissão de escrita.
        else:
            permissoes_atual &= ~stat.S_IWUSR  # Remove a permissão de escrita.

    # Modifica a permissão de execução, se especificada.
    if execucao is not None:
        if execucao:
            permissoes_atual |= stat.S_IXUSR  # Adiciona a permissão de execução.
        else:
            permissoes_atual &= ~stat.S_IXUSR  # Remove a permissão de execução.

    os.chmod(arquivo, permissoes_atual)  # Aplica as novas permissões ao arquivo usando chmod.

# Exemplo de uso
arquivo = input("Digite o caminho do arquivo para verificar permissões: ")  # Solicita ao usuário o caminho do arquivo.

# Verificar permissões atuais
permissoes = verificar_permissoes(arquivo)  # Chama a função para verificar as permissões do arquivo.
print(f"Permissões atuais: Leitura: {permissoes['readable']}, Escrita: {permissoes['writable']}, Execução: {permissoes['executable']}")  # Exibe as permissões atuais.

# Modificar permissões
modificar = input("Deseja modificar permissões? (s/n): ")  # Pergunta ao usuário se ele deseja modificar as permissões.
if modificar.lower() == 's':  # Se a resposta for 's' (sim), continua.
    leitura = input("Permitir leitura? (s/n): ").lower() == 's'  # Pergunta se deve permitir leitura.
    escrita = input("Permitir escrita? (s/n): ").lower() == 's'  # Pergunta se deve permitir escrita.
    execucao = input("Permitir execução? (s/n): ").lower() == 's'  # Pergunta se deve permitir execução.

    modificar_permissoes(arquivo, leitura, escrita, execucao)  # Chama a função para modificar as permissões com base nas respostas do usuário.
    print("Permissões modificadas com sucesso!")  # Informa que as permissões foram modificadas.

# Verificar permissões após modificação
permissoes_modificadas = verificar_permissoes(arquivo)  # Verifica as permissões do arquivo após a modificação.
print(f"Novas permissões: Leitura: {permissoes_modificadas['readable']}, Escrita: {permissoes_modificadas['writable']}, Execução: {permissoes_modificadas['executable']}")  # Exibe as novas permissões.
