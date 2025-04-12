# Código original para refatoração
echo "
def calcular_estatisticas(numeros):
    total = 0
    media = 0
    for numero in numeros:
        total += numero
    media = total / len(numeros)
    
    variancia = 0
    for numero in numeros:
        variancia += (numero - media) ** 2
    variancia /= len(numeros)
    
    desvio_padrao = variancia ** 0.5
    
    print(f'Total: {total}, Média: {media}, Desvio Padrão: {desvio_padrao}')
    return total, media, desvio_padrao

numeros = [1, 2, 3, 4, 5]
calcular_estatisticas(numeros)
" > codigo_original.py

# Passo 1: Analisar o código e identificar problemas
# - Função longa que realiza várias operações diferentes.
# - Variáveis com nomes não descritivos.
# - Estrutura duplicada para calcular total e variância.

# Passo 2: Refatoração do código
echo "
def calcular_total(numeros):
    return sum(numeros)

def calcular_media(total, quantidade):
    return total / quantidade

def calcular_variancia(numeros, media):
    return sum((numero - media) ** 2 for numero in numeros) / len(numeros)

def calcular_desvio_padrao(variancia):
    return variancia ** 0.5

def calcular_estatisticas(numeros):
    total = calcular_total(numeros)
    media = calcular_media(total, len(numeros))
    variancia = calcular_variancia(numeros, media)
    desvio_padrao = calcular_desvio_padrao(variancia)
    
    print(f'Total: {total}, Média: {media}, Desvio Padrão: {desvio_padrao}')
    return total, media, desvio_padrao

numeros = [1, 2, 3, 4, 5]
calcular_estatisticas(numeros)
" > codigo_refatorado.py

# Passo 3: Reexecutar o código para garantir que a funcionalidade foi preservada
python3 codigo_refatorado.py
