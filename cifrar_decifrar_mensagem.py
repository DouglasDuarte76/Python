from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def cifrar_mensagem(mensagem, chave):
    # Gerar um vetor de inicialização (IV) aleatório
    iv = get_random_bytes(16)
    # Criar um objeto de cifra AES em modo CBC
    cipher = AES.new(chave, AES.MODE_CBC, iv)
    # Cifrar a mensagem
    mensagem_cifrada = cipher.encrypt(pad(mensagem.encode(), AES.block_size))
    return iv + mensagem_cifrada

def decifrar_mensagem(mensagem_cifrada, chave):
    # Extrair o IV dos primeiros 16 bytes da mensagem cifrada
    iv = mensagem_cifrada[:16]
    # Extrair a mensagem cifrada
    mensagem_cifrada = mensagem_cifrada[16:]
    # Criar um objeto de cifra AES em modo CBC
    cipher = AES.new(chave, AES.MODE_CBC, iv)
    # Decifrar a mensagem
    mensagem_decifrada = unpad(cipher.decrypt(mensagem_cifrada), AES.block_size)
    return mensagem_decifrada.decode()

# Definir a chave (deve ter 16, 24 ou 32 bytes)
chave = get_random_bytes(16)

# Solicitar mensagem do usuário
mensagem = input("Digite uma mensagem para cifrar: ")

# Cifrar a mensagem
mensagem_cifrada = cifrar_mensagem(mensagem, chave)
print(f"Mensagem Cifrada: {mensagem_cifrada}")

# Decifrar a mensagem
mensagem_decifrada = decifrar_mensagem(mensagem_cifrada, chave)
print(f"Mensagem Decifrada: {mensagem_decifrada}")
