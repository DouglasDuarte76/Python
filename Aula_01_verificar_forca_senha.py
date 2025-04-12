import re

def verificar_forca_senha(senha):
    # Critérios de senha
    comprimento_minimo = 8
    maiuscula = re.compile(r'[A-Z]')
    minuscula = re.compile(r'[a-z]')
    numero = re.compile(r'\d')
    caractere_especial = re.compile(r'[!@#$%^&*(),.?":{}|<>]')

    # Verificação dos critérios
    if len(senha) < comprimento_minimo:
        return "Senha fraca: deve ter pelo menos 8 caracteres."
    if not maiuscula.search(senha):
        return "Senha fraca: deve conter pelo menos uma letra maiúscula."
    if not minuscula.search(senha):
        return "Senha fraca: deve conter pelo menos uma letra minúscula."
    if not numero.search(senha):
        return "Senha fraca: deve conter pelo menos um número."
    if not caractere_especial.search(senha):
        return "Senha fraca: deve conter pelo menos um caractere especial."
    
    return "Senha forte!"

# Solicitar senha do usuário
senha = input("Digite uma senha para verificar sua força: ")
resultado = verificar_forca_senha(senha)
print(resultado)
