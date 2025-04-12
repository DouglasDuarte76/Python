import psutil
import time

# Definir os limites para o uso de recursos
LIMITE_CPU = 80  # Porcentagem
LIMITE_MEMORIA = 70  # Porcentagem
LIMITE_DISCO = 90  # Porcentagem

# Função para monitorar o desempenho do sistema
def monitorar_desempenho():
    alertas = []
    
    # Monitorar o uso de CPU
    uso_cpu = psutil.cpu_percent(interval=1)
    if uso_cpu > LIMITE_CPU:
        alertas.append(f"Alerta: Uso de CPU em {uso_cpu}% (acima do limite de {LIMITE_CPU}%)")
    
    # Monitorar o uso de memória
    uso_memoria = psutil.virtual_memory().percent
    if uso_memoria > LIMITE_MEMORIA:
        alertas.append(f"Alerta: Uso de Memória em {uso_memoria}% (acima do limite de {LIMITE_MEMORIA}%)")
    
    # Monitorar o uso de disco
    uso_disco = psutil.disk_usage('/').percent
    if uso_disco > LIMITE_DISCO:
        alertas.append(f"Alerta: Uso de Disco em {uso_disco}% (acima do limite de {LIMITE_DISCO}%)")
    
    return alertas

# Função principal para executar o monitoramento em intervalos de tempo
def executar_monitoramento(intervalo=10):
    while True:
        alertas = monitorar_desempenho()
        
        if alertas:
            print("Alertas detectados:")
            for alerta in alertas:
                print(f"- {alerta}")
        else:
            print("Desempenho dentro dos limites.")
        
        # Aguardar o próximo intervalo
        time.sleep(intervalo)

# Executar o monitoramento com intervalo de 10 segundos
executar_monitoramento(intervalo=10)


_____


# Função para registrar alertas e desempenho no arquivo de log
def registrar_log(alertas):
    with open('log_desempenho.txt', 'a') as f:
        if alertas:
            for alerta in alertas:
                f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {alerta}\n")
        else:
            f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Desempenho dentro dos limites.\n")

# Modificar o monitoramento para incluir o registro em log
def executar_monitoramento_com_log(intervalo=10):
    while True:
        alertas = monitorar_desempenho()
        
        if alertas:
            print("Alertas detectados:")
            for alerta in alertas:
                print(f"- {alerta}")
        
        # Registrar o desempenho no log
        registrar_log(alertas)
        
        # Aguardar o próximo intervalo
        time.sleep(intervalo)

# Executar o monitoramento com registro em log
executar_monitoramento_com_log(intervalo=10)


_____


