pip install scapy pandas matplotlib

import scapy.all as scapy
import pandas as pd
import time
import matplotlib.pyplot as plt

# Dicionário para armazenar contagem de IPs
trafego = {}

# Função para processar pacotes de rede
def processar_pacote(pacote):
    if pacote.haslayer(scapy.IP):  # Verifica se o pacote contém um IP
        ip_origem = pacote[scapy.IP].src
        
        if ip_origem in trafego:
            trafego[ip_origem] += 1
        else:
            trafego[ip_origem] = 1

        # Verifica se um IP está enviando tráfego excessivo (possível ataque DDoS)
        if trafego[ip_origem] > 50:
            print(f"[ALERTA] Tráfego suspeito detectado do IP: {ip_origem}")

# Captura de pacotes em tempo real por 30 segundos
print("Monitorando tráfego de rede...")
scapy.sniff(prn=processar_pacote, timeout=30)

# Criar DataFrame para visualização dos dados
df = pd.DataFrame(list(trafego.items()), columns=['IP', 'Pacotes'])
df = df.sort_values(by='Pacotes', ascending=False)

# Exibir tabela com IPs monitorados
print("\nResumo do tráfego monitorado:")
print(df)

# Plotar gráfico de tráfego de rede
plt.figure(figsize=(10, 5))
plt.bar(df['IP'], df['Pacotes'])
plt.xticks(rotation=90)
plt.xlabel("IP de Origem")
plt.ylabel("Número de Pacotes")
plt.title("Monitoramento de Tráfego em Dispositivo Edge")
plt.show()

