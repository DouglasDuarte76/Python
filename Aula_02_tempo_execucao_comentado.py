import time  # Importa o módulo time para medir o tempo de execução.

# Decorator para medir o tempo de execução de uma função.
def tempo_de_execucao(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()  # Marca o tempo de início.
        resultado = func(*args, **kwargs)  # Executa a função original e armazena o resultado.
        fim = time.time()  # Marca o tempo de fim.
        print(f"Tempo de execução: {fim - inicio:.4f} segundos")  # Calcula e imprime o tempo total de execução.
        return resultado  # Retorna o resultado da função original.
    return wrapper  # Retorna o wrapper, que substitui a função original.

@tempo_de_execucao  # Aplica o decorator à função encontrar_primos, medindo o tempo de execução.
def encontrar_primos(limite):
    primos = []  # Cria uma lista vazia para armazenar os números primos.
    for num in range(2, limite + 1):  # Itera sobre todos os números de 2 até o limite.
        for i in range(2, int(num**0.5) + 1):  # Verifica se num é divisível por qualquer número até a raiz quadrada de num.
            if num % i == 0:  # Se num for divisível, ele não é primo.
                break  # Sai do loop interno se num não for primo.
        else:  # Se num não foi divisível por nenhum número no loop interno, ele é primo.
            primos.append(num)  # Adiciona o número primo à lista de primos.
    return primos  # Retorna a lista de números primos.

# Generator para produzir números primos indefinidamente.
def gerar_primos():
    num = 2  # Inicia a verificação a partir do número 2.
    while True:  # Loop infinito para gerar primos continuamente.
        for i in range(2, int(num**0.5) + 1):  # Verifica se num é divisível por qualquer número até a raiz quadrada de num.
            if num % i == 0:  # Se num for divisível, ele não é primo.
                break  # Sai do loop interno se num não for primo.
        else:  # Se num não foi divisível por nenhum número no loop interno, ele é primo.
            yield num  # Gera o número primo e o retorna sem interromper a execução do generator.
        num += 1  # Incrementa num para testar o próximo número.

# Testando o decorator com a função de encontrar primos
primos = encontrar_primos(100)  # Encontra todos os números primos até 100 e mede o tempo de execução.
print(primos)  # Imprime a lista de números primos encontrados.

# Testando o generator de primos
generator_primos = gerar_primos()  # Cria um generator para produzir números primos.
for _ in range(10):  # Gera e imprime os 10 primeiros números primos.
    print(next(generator_primos))  # Obtém o próximo número primo do generator.
