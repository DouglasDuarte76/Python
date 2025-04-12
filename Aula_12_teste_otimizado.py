import timeit
import cProfile
import pstats

# Exemplo de código para medir com timeit
def processamento_dados(data):
    result = [x * 2 for x in data if x % 2 == 0]
    return sum(result)

data = list(range(1000000))

# Passo 2: Medindo o tempo de execução da função
tempo_execucao = timeit.timeit("processamento_dados(data)", globals=globals(), number=10)
print(f"Tempo médio de execução: {tempo_execucao:.4f} segundos")

# Passo 3: Analisando a performance com cProfile
def run_profile():
    processamento_dados(data)

cProfile.run('run_profile()', 'perfil.txt')

# Analisando o perfil de execução gerado
with open('perfil.txt', 'r') as f:
    print(f.read())

# Passo 4: Sugestão de otimização (exemplo simples)
def processamento_dados_otimizado(data):
    result = sum(x * 2 for x in data if x % 2 == 0)
    return result

# Reexecução do perfil após otimização
cProfile.run('processamento_dados_otimizado(data)')
