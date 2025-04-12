pip install pyseal

import random

# Parâmetros de criptografia
P = 97  # Número primo grande para modular as operações

# Função para gerar chave de criptografia (aleatória)
def gerar_chave():
    return random.randint(1, P-1)

# Função para criptografar um número
def criptografar(mensagem, chave):
    return (mensagem + chave) % P

# Função para descriptografar um número
def descriptografar(mensagem_cifrada, chave):
    return (mensagem_cifrada - chave) % P

# Função para soma de números criptografados
def soma_homomorfica(c1, c2):
    return (c1 + c2) % P

# Geração de chave secreta
chave_secreta = gerar_chave()

# Exemplo de operação homomórfica
num1 = 15
num2 = 27

# Criptografando números
c1 = criptografar(num1, chave_secreta)
c2 = criptografar(num2, chave_secreta)

# Somando valores criptografados
soma_cifrada = soma_homomorfica(c1, c2)

# Descriptografando o resultado
soma_original = descriptografar(soma_cifrada, chave_secreta)

# Exibindo resultados
print(f"Número 1: {num1}, Número 2: {num2}")
print(f"Valores Criptografados: {c1}, {c2}")
print(f"Soma Criptografada: {soma_cifrada}")
print(f"Soma Descriptografada: {soma_original}")

