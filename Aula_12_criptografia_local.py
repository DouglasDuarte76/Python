pip install boto3 cryptography

import boto3
from cryptography.fernet import Fernet

# Gerar e armazenar chave de criptografia
chave = Fernet.generate_key()
cipher_suite = Fernet(chave)

# Função para criptografar um arquivo
def criptografar_arquivo(nome_arquivo):
    with open(nome_arquivo, 'rb') as file:
        arquivo_dados = file.read()
    
    arquivo_criptografado = cipher_suite.encrypt(arquivo_dados)
    
    with open(f"criptografado_{nome_arquivo}", 'wb') as file_enc:
        file_enc.write(arquivo_criptografado)
    
    print(f"Arquivo '{nome_arquivo}' criptografado com sucesso.")

# Função para enviar arquivo criptografado para AWS S3
def enviar_para_s3(bucket_name, arquivo):
    s3 = boto3.client('s3')
    try:
        s3.upload_file(arquivo, bucket_name, arquivo)
        print(f"Arquivo '{arquivo}' enviado para o bucket '{bucket_name}' com sucesso.")
    except Exception as e:
        print(f"Erro ao enviar arquivo para S3: {e}")

# Nome do arquivo a ser criptografado e enviado
nome_arquivo = "dados_sensiveis.txt"

# Criptografar o arquivo
criptografar_arquivo(nome_arquivo)

# Enviar para S3
enviar_para_s3("meu-bucket-seguro", f"criptografado_{nome_arquivo}")
