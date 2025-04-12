from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization

# Gerar um par de chaves RSA (chave privada e chave pública)
chave_privada = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
chave_publica = chave_privada.public_key()

# Função para cifrar uma mensagem usando a chave pública
def cifrar_mensagem(mensagem, chave_publica):
    mensagem_cifrada = chave_publica.encrypt(
        mensagem.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return mensagem_cifrada

# Função para decifrar uma mensagem usando a chave privada
def decifrar_mensagem(mensagem_cifrada, chave_privada):
    mensagem_decifrada = chave_privada.decrypt(
        mensagem_cifrada,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return mensagem_decifrada.decode()

# Solicitar mensagem do usuário
mensagem = input("Digite uma mensagem para cifrar: ")

# Cifrar a mensagem com a chave pública
mensagem_cifrada = cifrar_mensagem(mensagem, chave_publica)
print(f"Mensagem Cifrada: {mensagem_cifrada}")

# Decifrar a mensagem com a chave privada
mensagem_decifrada = decifrar_mensagem(mensagem_cifrada, chave_privada)
print(f"Mensagem Decifrada: {mensagem_decifrada}")

# (Opcional) Exportar as chaves para arquivos
chave_privada_pem = chave_privada.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)

chave_publica_pem = chave_publica.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Salvar as chaves em arquivos
with open("chave_privada.pem", "wb") as f:
    f.write(chave_privada_pem)

with open("chave_publica.pem", "wb") as f:
    f.write(chave_publica_pem)
