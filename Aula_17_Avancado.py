pip install scapy pandas matplotlib

import scapy.all as scapy
import pandas as pd
import time
import matplotlib.pyplot as plt

# Dicionário para armazenar contagem de IPs e comandos enviados
trafego_ics = {}

# Função para processar pacotes Modbus/TCP
def processar_pacote(pacote):
    if pacote.haslayer(scapy.IP) and pacote.haslayer(scapy.TCP):
        ip_origem = pacote[scapy.IP].src
        porta_destino = pacote[scapy.TCP].dport

        # Detectar tráfego Modbus (porta 502)
        if porta_destino == 502:
            print(f"[ALERTA] Tráfego Modbus detectado de {ip_origem}")

            if ip_origem in trafego_ics:
                trafego_ics[ip_origem] += 1
            else:
                trafego_ics[ip_origem] = 1

            # Detectar acessos excessivos (potencial ataque)
            if trafego_ics[ip_origem] > 10:
                print(f"[ATAQUE] IP {ip_origem} enviou múltiplos comandos suspeitos para Modbus!")

# Captura de pacotes por 30 segundos
print("Monitorando tráfego ICS...")
scapy.sniff(prn=processar_pacote, timeout=30)

# Criar DataFrame para visualização dos dados
df = pd.DataFrame(list(trafego_ics.items()), columns=['IP', 'Pacotes'])
df = df.sort_values(by='Pacotes', ascending=False)

# Exibir tabela com IPs monitorados
print("\nResumo do tráfego ICS monitorado:")
print(df)

# Plotar gráfico de tráfego Modbus
plt.figure(figsize=(10, 5))
plt.bar(df['IP'], df['Pacotes'])
plt.xticks(rotation=90)
plt.xlabel("IP de Origem")
plt.ylabel("Número de Pacotes Modbus")
plt.title("Monitoramento de Tráfego ICS (Modbus)")
plt.show()
