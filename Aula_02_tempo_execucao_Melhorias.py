import time
from functools import wraps

# Decorator para medir tempo de execução
def tempo_de_execucao(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"Tempo de execução de {func.__name__}: {fim - inicio:.4f} segundos")
        return resultado
    return wrapper

@tempo_de_execucao
def encontrar_primos(limite):
    primos = []
    for num in range(2, limite + 1):
        eh_primo = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                eh_primo = False
                break
        if eh_primo:
            primos.append(num)
    return primos

# Generator para produzir números primos
def gerar_primos():
    num = 2
    while True:
        eh_primo = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                eh_primo = False
                break
        if eh_primo:
            yield num
        num += 1

# Testando o decorator com a função de encontrar primos
if __name__ == "__main__":
    primos = encontrar_primos(100)
    print(f"Primos até 100: {primos}")

    # Testando o generator de primos
    generator_primos = gerar_primos()
    for _ in range(10):
        print(next(generator_primos))
