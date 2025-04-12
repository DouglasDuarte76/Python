import asyncio
import time

# Passo 1: Criar corrotinas que simulam chamadas de API
async def chamada_api_simulada(nome, atraso):
    print(f"Começando a {nome}")
    await asyncio.sleep(atraso)  # Simula uma operação de I/O com atraso
    print(f"Concluindo a {nome}")
    return f"{nome} concluída"

# Passo 2: Executar corrotinas de forma concorrente usando asyncio.gather
async def main():
    inicio = time.time()
    
    tarefas = [
        chamada_api_simulada("chamada 1", 2),
        chamada_api_simulada("chamada 2", 1),
        chamada_api_simulada("chamada 3", 3)
    ]
    
    resultados = await asyncio.gather(*tarefas)
    
    fim = time.time()
    print(f"Todas as chamadas concluídas em {fim - inicio:.2f} segundos")
    print("Resultados:", resultados)

# Executar o loop de eventos
asyncio.run(main())

# Para comparar, podemos implementar uma versão síncrona das mesmas operações:
def chamada_api_simulada_sincrona(nome, atraso):
    print(f"Começando a {nome}")
    time.sleep(atraso)  # Operação de I/O bloqueante
    print(f"Concluindo a {nome}")
    return f"{nome} concluída"

def main_sincrono():
    inicio = time.time()
    
    resultados = [
        chamada_api_simulada_sincrona("chamada 1", 2),
        chamada_api_simulada_sincrona("chamada 2", 1),
        chamada_api_simulada_sincrona("chamada 3", 3)
    ]
    
    fim = time.time()
    print(f"Todas as chamadas concluídas em {fim - inicio:.2f} segundos")
    print("Resultados:", resultados)

# Comparação:
print("Execução síncrona:")
main_sincrono()

print("\nExecução assíncrona:")
asyncio.run(main())
