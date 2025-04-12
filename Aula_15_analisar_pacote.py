from scapy.all import sniff
from collections import defaultdict
import time

# Dicionário para contar tentativas de conexão em diferentes portas
tentativas_portas = defaultdict(int)
# Dicionário para armazenar o tempo da última tentativa de conexão
ultimo_acesso = defaultdict(float)

# Função para processar pacotes de rede
def analisar_pacote(pacote):
    if pacote.haslayer('IP'):
        ip_origem = pacote['IP'].src
        porta_destino = pacote['TCP'].dport if pacote.haslayer('TCP') else None

        # Contar tentativas de conexão por IP e porta
        if porta_destino:
            tentativas_portas[(ip_origem, porta_destino)] += 1
            tempo_atual = time.time()
            
            # Verificar se houve várias tentativas em um curto período de tempo
            if (tempo_atual - ultimo_acesso[ip_origem]) < 10:  # Intervalo de 10 segundos
                print(f"Alerta: Tentativa suspeita de escaneamento de portas do IP {ip_origem}")
            
            # Atualizar o tempo de última tentativa de acesso
            ultimo_acesso[ip_origem] = tempo_atual

# Função para iniciar o monitoramento de rede
def monitorar_rede():
    print("Monitorando tráfego de rede...")
    # Sniff de pacotes na interface de rede (substitua 'eth0' pela interface correta)
    sniff(prn=analisar_pacote, filter="tcp", store=0)

# Iniciar o monitoramento de rede
if __name__ == "__main__":
    monitorar_rede()

___


# Função para salvar alertas em um arquivo
def salvar_alertas_em_arquivo(alerta, arquivo_saida='alertas_rede.txt'):
    with open(arquivo_saida, 'a') as f:
        f.write(f"{alerta}\n")

# Modificar o monitoramento para salvar alertas em um arquivo
def analisar_pacote_modificado(pacote):
    if pacote.haslayer('IP'):
        ip_origem = pacote['IP'].src
        porta_destino = pacote['TCP'].dport if pacote.haslayer('TCP') else None

        if porta_destino:
            tentativas_portas[(ip_origem, porta_destino)] += 1
            tempo_atual = time.time()

            if (tempo_atual - ultimo_acesso[ip_origem]) < 10:
                alerta = f"Alerta: Tentativa suspeita de escaneamento de portas do IP {ip_origem}"
                print(alerta)
                salvar_alertas_em_arquivo(alerta)

            ultimo_acesso[ip_origem] = tempo_atual

# Iniciar o monitoramento com salvamento de alertas
monitorar_rede()

___


