from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization

def gerar_par_chaves():
    """Gera um par de chaves RSA (privada e pública)."""
    try:
        chave_privada = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        chave_publica = chave_privada.public_key()
        return chave_privada, chave_publica
    except Exception as e:
        print(f"Erro ao gerar par de chaves: {e}")
        return None, None

def cifrar_mensagem(mensagem, chave_publica):
    """Cifra uma mensagem usando a chave pública."""
    try:
        mensagem_cifrada = chave_publica.encrypt(
            mensagem.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return mensagem_cifrada
    except Exception as e:
        print(f"Erro ao cifrar a mensagem: {e}")
        return None

def decifrar_mensagem(mensagem_cifrada, chave_privada):
    """Decifra uma mensagem usando a chave privada."""
    try:
        mensagem_decifrada = chave_privada.decrypt(
            mensagem_cifrada,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return mensagem_decifrada.decode()
    except Exception as e:
        print(f"Erro ao decifrar a mensagem: {e}")
        return None

def salvar_chaves_em_arquivo(chave_privada, chave_publica):
    """Salva as chaves privada e pública em arquivos."""
    try:
        chave_privada_pem = chave_privada.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()  # Considere usar uma senha aqui
        )

        chave_publica_pem = chave_publica.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        with open("chave_privada.pem", "wb") as f:
            f.write(chave_privada_pem)

        with open("chave_publica.pem", "wb") as f:
            f.write(chave_publica_pem)

        print("Chaves salvas em 'chave_privada.pem' e 'chave_publica.pem'.")
    except Exception as e:
        print(f"Erro ao salvar as chaves em arquivo: {e}")

def main():
    # Gerar par de chaves
    chave_privada, chave_publica = gerar_par_chaves()
    if not chave_privada or not chave_publica:
        return

    # Solicitar mensagem do usuário
    mensagem = input("Digite uma mensagem para cifrar: ").strip()
    if not mensagem:
        print("A mensagem não pode estar vazia.")
        return

    # Cifrar a mensagem
    mensagem_cifrada = cifrar_mensagem(mensagem, chave_publica)
    if mensagem_cifrada:
        print(f"Mensagem Cifrada: {mensagem_cifrada}")

    # Decifrar a mensagem
    mensagem_decifrada = decifrar_mensagem(mensagem_cifrada, chave_privada)
    if mensagem_decifrada:
        print(f"Mensagem Decifrada: {mensagem_decifrada}")

    # Salvar as chaves em arquivos
    salvar_chaves_em_arquivo(chave_privada, chave_publica)

if __name__ == "__main__":
    main()
