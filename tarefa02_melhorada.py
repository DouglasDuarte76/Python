from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

def cifrar_mensagem(mensagem, chave):
    if not mensagem:
        raise ValueError("A mensagem não pode estar vazia.")
    if len(chave) not in [16, 24, 32]:
        raise ValueError("A chave deve ter 16, 24 ou 32 bytes de comprimento.")

    # Gerar um vetor de inicialização (IV) aleatório
    iv = get_random_bytes(16)
    # Criar um objeto de cifra AES em modo CBC
    cipher = AES.new(chave, AES.MODE_CBC, iv)
    # Cifrar a mensagem
    mensagem_cifrada = cipher.encrypt(pad(mensagem.encode(), AES.block_size))
    # Retornar a mensagem cifrada junto com o IV codificados em base64
    return base64.b64encode(iv + mensagem_cifrada).decode('utf-8')

def decifrar_mensagem(mensagem_cifrada, chave):
    if len(chave) not in [16, 24, 32]:
        raise ValueError("A chave deve ter 16, 24 ou 32 bytes de comprimento.")

    # Decodificar a mensagem cifrada de base64
    mensagem_cifrada = base64.b64decode(mensagem_cifrada)

    # Extrair o IV dos primeiros 16 bytes da mensagem cifrada
    iv = mensagem_cifrada[:16]
    # Extrair a mensagem cifrada
    mensagem_cifrada = mensagem_cifrada[16:]
    # Criar um objeto de cifra AES em modo CBC
    cipher = AES.new(chave, AES.MODE_CBC, iv)
    # Decifrar a mensagem
    mensagem_decifrada = unpad(cipher.decrypt(mensagem_cifrada), AES.block_size)
    return mensagem_decifrada.decode('utf-8')

# Definir a chave (deve ter 16, 24 ou 32 bytes)
chave = get_random_bytes(16)

# Solicitar mensagem do usuário
mensagem = input("Digite uma mensagem para cifrar: ")

try:
    # Cifrar a mensagem
    mensagem_cifrada = cifrar_mensagem(mensagem, chave)
    print(f"Mensagem Cifrada: {mensagem_cifrada}")

    # Decifrar a mensagem
    mensagem_decifrada = decifrar_mensagem(mensagem_cifrada, chave)
    print(f"Mensagem Decifrada: {mensagem_decifrada}")
except ValueError as ve:
    print(f"Erro: {ve}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
