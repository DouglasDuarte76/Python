import hashlib
import os

# Função para gerar hash de uma string
def gerar_hash_string(data, algoritmo='sha256'):
    if algoritmo == 'md5':
        hash_obj = hashlib.md5(data.encode())
    elif algoritmo == 'sha1':
        hash_obj = hashlib.sha1(data.encode())
    elif algoritmo == 'sha256':
        hash_obj = hashlib.sha256(data.encode())
    else:
        raise ValueError("Algoritmo de hash não suportado.")
    
    return hash_obj.hexdigest()

# Função para verificar integridade de arquivo
def verificar_integridade_arquivo(caminho_arquivo, hash_original, algoritmo='sha256'):
    with open(caminho_arquivo, 'rb') as file:
        conteudo = file.read()
    
    hash_atual = gerar_hash_string(conteudo.decode(), algoritmo)
    
    return hash_atual == hash_original

# Teste das funções
texto = "Segurança da Informação"
hash_texto = gerar_hash_string(texto, 'sha256')
print(f"Hash do texto: {hash_texto}")

# Gerar hash de um arquivo de exemplo
arquivo = 'exemplo.txt'
with open(arquivo, 'w') as f:
    f.write(texto)

hash_arquivo = gerar_hash_string(open(arquivo, 'r').read(), 'sha256')
print(f"Hash do arquivo '{arquivo}': {hash_arquivo}")

# Verificar integridade do arquivo
integridade = verificar_integridade_arquivo(arquivo, hash_arquivo, 'sha256')
print(f"Integridade do arquivo verificada: {integridade}")
