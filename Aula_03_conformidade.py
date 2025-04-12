# Código original fornecido para refatoração
def calc(a,b):
 s=a+b
 t=a*b
 if a>b:
    return s
 else:
    return t
result=calc(5,3)
print(result)

# Código refatorado seguindo boas práticas
def calcular_soma_e_produto(num1, num2):
    """Calcula a soma e o produto de dois números.
    
    Retorna a soma se o primeiro número for maior que o segundo, 
    caso contrário, retorna o produto.
    """
    soma = num1 + num2
    produto = num1 * num2
    
    if num1 > num2:
        return soma
    return produto

resultado = calcular_soma_e_produto(5, 3)
print(resultado)
