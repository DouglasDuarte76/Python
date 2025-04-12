import re

def verificar_forca_senha(senha):
    # Critérios de senha
    comprimento_minimo = 12
    maiuscula = re.compile(r'[A-Z]')
    minuscula = re.compile(r'[a-z]')
    numero = re.compile(r'\d')
    caractere_especial = re.compile(r'[!@#$%^&*(),.?":{}|<>]')
    sequencia = re.compile(r'(.)\1{2,}')  # Três ou mais caracteres repetidos
    espaco_branco = re.compile(r'\s')
    senhas_comuns = [
        "123456", "password", "123456789", "12345678", "12345", 
        "1234567", "qwerty", "abc123", "111111", "123123"
    ]
    
    # Verificação dos critérios
    if len(senha) < comprimento_minimo:
        return "Senha fraca: deve ter pelo menos 12 caracteres."
    if senha in senhas_comuns:
        return "Senha fraca: evite usar senhas comuns."
    if espaco_branco.search(senha):
        return "Senha fraca: não deve conter espaços em branco."
    if sequencia.search(senha):
        return "Senha fraca: não deve conter sequências de caracteres repetidos."
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
