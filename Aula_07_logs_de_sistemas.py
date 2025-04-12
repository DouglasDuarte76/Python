import os
import subprocess
from datetime import datetime

# Função para coletar logs do sistema
def coletar_logs_sistema():
    logs = subprocess.getoutput('dmesg')
    with open(f"logs_sistema_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log", 'w') as f:
        f.write(logs)
    print("Logs do sistema coletados e armazenados.")

# Função para coletar conexões de rede ativas
def coletar_conexoes_rede():
    conexoes = subprocess.getoutput('netstat -tulnp')
    with open(f"conexoes_rede_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log", 'w') as f:
        f.write(conexoes)
    print("Conexões de rede ativas coletadas e armazenadas.")

# Função para listar processos em execução
def listar_processos():
    processos = subprocess.getoutput('ps aux')
    with open(f"processos_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log", 'w') as f:
        f.write(processos)
    print("Processos em execução coletados e armazenados.")

# Executar funções de coleta de informações
coletar_logs_sistema()
coletar_conexoes_rede()
listar_processos()
