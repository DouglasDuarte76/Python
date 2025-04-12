# Importa o backend padrão da biblioteca cryptography, que será utilizado para gerar as chaves RSA
from cryptography.hazmat.backends import default_backend

# Importa as funções necessárias para operações assimétricas de RSA e para definir o padding (preenchimento)
from cryptography.hazmat.primitives.asymmetric import rsa, padding

# Importa funções para calcular hashes (necessário para o padding OAEP)
from cryptography.hazmat.primitives import hashes

# Importa funções para serialização das chaves, que serão usadas para salvar/exportar as chaves em formato PEM
from cryptography.hazmat.primitives import serialization

# Gera um par de chaves RSA (chave privada e chave pública)
chave_privada = rsa.generate_private_key(
    public_exponent=65537,  # Exponente público padrão recomendado para RSA
    key_size=2048,          # Tamanho da chave em bits (2048 é seguro para a maioria das aplicações)
    backend=default_backend()  # Backend utilizado para realizar a operação de geração da chave
)

# Extrai a chave pública a partir da chave privada
chave_publica = chave_privada.public_key()

# Função para cifrar uma mensagem utilizando a chave pública
def cifrar_mensagem(mensagem, chave_publica):
    # Cifra a mensagem usando a chave pública, com o padding OAEP e o hash SHA-256
    mensagem_cifrada = chave_publica.encrypt(
        mensagem.encode(),  # Converte a mensagem de string para bytes
        padding.OAEP(  # Define o esquema de padding OAEP com SHA-256
            mgf=padding.MGF1(algorithm=hashes.SHA256()),  # Gerador de máscara baseado em SHA-256
            algorithm=hashes.SHA256(),  # Algoritmo de hash utilizado (SHA-256)
            label=None  # Opcional, mas geralmente não é utilizado no OAEP
        )
    )
    return mensagem_cifrada  # Retorna a mensagem cifrada em bytes

# Função para decifrar uma mensagem usando a chave privada
def decifrar_mensagem(mensagem_cifrada, chave_privada):
    # Decifra a mensagem cifrada usando a chave privada e o mesmo padding OAEP com SHA-256
    mensagem_decifrada = chave_privada.decrypt(
        mensagem_cifrada,  # A mensagem cifrada a ser decifrada
        padding.OAEP(  # Define o mesmo esquema de padding usado na cifragem
            mgf=padding.MGF1(algorithm=hashes.SHA256()),  # Gerador de máscara com SHA-256
            algorithm=hashes.SHA256(),  # Algoritmo de hash (SHA-256)
            label=None  # Label opcional (não utilizado)
        )
    )
    return mensagem_decifrada.decode()  # Retorna a mensagem decifrada, convertida de bytes para string

# Solicita que o usuário insira uma mensagem para ser cifrada
mensagem = input("Digite uma mensagem para cifrar: ")

# Cifra a mensagem utilizando a chave pública
mensagem_cifrada = cifrar_mensagem(mensagem, chave_publica)
print(f"Mensagem Cifrada: {mensagem_cifrada}")  # Exibe a mensagem cifrada

# Decifra a mensagem utilizando a chave privada
mensagem_decifrada = decifrar_mensagem(mensagem_cifrada, chave_privada)
print(f"Mensagem Decifrada: {mensagem_decifrada}")  # Exibe a mensagem decifrada

# (Opcional) Exportar a chave privada para o formato PEM
chave_privada_pem = chave_privada.private_bytes(
    encoding=serialization.Encoding.PEM,  # Codificação PEM (base64)
    format=serialization.PrivateFormat.TraditionalOpenSSL,  # Formato tradicional do OpenSSL
    encryption_algorithm=serialization.NoEncryption()  # Sem criptografia para proteger a chave privada
)

# Exportar a chave pública para o formato PEM
chave_publica_pem = chave_publica.public_bytes(
    encoding=serialization.Encoding.PEM,  # Codificação PEM
    format=serialization.PublicFormat.SubjectPublicKeyInfo  # Formato público padrão
)

# Salvar a chave privada em um arquivo "chave_privada.pem"
with open("chave_privada.pem", "wb") as f:
    f.write(chave_privada_pem)  # Escreve a chave privada no arquivo

# Salvar a chave pública em um arquivo "chave_publica.pem"
with open("chave_publica.pem", "wb") as f:
    f.write(chave_publica_pem)  # Escreve a chave pública no arquivo
