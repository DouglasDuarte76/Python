pip install hashlib pefile yara-python

import hashlib
import pefile
import yara
import os

# Função para calcular hash SHA-256 de um arquivo
def calcular_hash(arquivo):
    hasher = hashlib.sha256()
    with open(arquivo, "rb") as f:
        while chunk := f.read(4096):
            hasher.update(chunk)
    return hasher.hexdigest()

# Função para extrair informações PE (arquivos executáveis Windows)
def extrair_info_pe(arquivo):
    try:
        pe = pefile.PE(arquivo)
        info = {
            "Entry Point": hex(pe.OPTIONAL_HEADER.AddressOfEntryPoint),
            "Image Base": hex(pe.OPTIONAL_HEADER.ImageBase),
            "Número de Seções": len(pe.sections)
        }
        return info
    except Exception as e:
        return {"Erro": str(e)}

# Criar regras YARA para detectar malware (exemplo simples)
regra_yara = """
rule MalwareSample {
    strings:
        $malicious_str = "malware"
        $api_call = "CreateRemoteThread"
    condition:
        any of them
}
"""

# Função para analisar arquivo com YARA
def analisar_yara(arquivo):
    rules = yara.compile(source=regra_yara)
    matches = rules.match(arquivo)
    return [str(match) for match in matches]

# Função principal para análise de malware
def analisar_malware(arquivo):
    print(f"\nAnalisando o arquivo: {arquivo}")

    # Cálculo de hash
    hash_arquivo = calcular_hash(arquivo)
    print(f"SHA-256: {hash_arquivo}")

    # Extração de informações PE
    info_pe = extrair_info_pe(arquivo)
    print("Informações PE:", info_pe)

    # Verificação de assinaturas YARA
    assinaturas = analisar_yara(arquivo)
    if assinaturas:
        print(f"[ALERTA] Padrões maliciosos detectados: {assinaturas}")
    else:
        print("Nenhum padrão suspeito encontrado.")

# Caminho do arquivo a ser analisado
arquivo_teste = "sample.exe"  # Substituir por um arquivo real para teste
if os.path.exists(arquivo_teste):
    analisar_malware(arquivo_teste)
else:
    print("Arquivo de teste não encontrado.")
