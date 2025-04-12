import time

# Decorator para medir tempo de execução
def tempo_de_execucao(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"Tempo de execução: {fim - inicio:.4f} segundos")
        return resultado
    return wrapper

@tempo_de_execucao
def encontrar_primos(limite):
    primos = []
    for num in range(2, limite + 1):
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            primos.append(num)
    return primos

# Generator para produzir números primos
def gerar_primos():
    num = 2
    while True:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            yield num
        num += 1

# Testando o decorator com a função de encontrar primos
primos = encontrar_primos(100)
print(primos)

# Testando o generator de primos
generator_primos = gerar_primos()
for _ in range(10):
    print(next(generator_primos))

______________________________________________________________

