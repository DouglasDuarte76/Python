from scapy.all import sniff, TCP, IP

# Função para analisar pacotes capturados
def analisar_pacote(pacote):
    # Verificar se o pacote é do tipo HTTP (porta 80)
    if pacote.haslayer(TCP) and pacote[TCP].dport == 80:
        print(f"[+] Pacote HTTP Capturado: {pacote[IP].src} -> {pacote[IP].dst}")
        print(f"    - Payload: {pacote[TCP].payload}")

# Função principal para captura de pacotes
def capturar_pacotes():
    print("Iniciando captura de pacotes HTTP...")
    sniff(prn=analisar_pacote, filter="tcp", store=0)

# Executar a captura de pacotes
capturar_pacotes()
