pip install pillow exifread


from PIL import Image
import exifread
import os

def extrair_metadados(caminho_arquivo):
    try:
        # Abrir a imagem e extrair metadados EXIF
        with open(caminho_arquivo, 'rb') as imagem:
            tags = exifread.process_file(imagem)
        
        # Exibir metadados relevantes
        if tags:
            print(f"Metadados da imagem '{caminho_arquivo}':")
            for tag in tags.keys():
                if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
                    print(f"{tag}: {tags[tag]}")
        else:
            print("Nenhum metadado EXIF encontrado.")
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")

# Solicitar o caminho do arquivo
caminho_arquivo = input("Digite o caminho do arquivo de imagem para análise de metadados: ")

# Verificar se o arquivo existe
if os.path.isfile(caminho_arquivo):
    extrair_metadados(caminho_arquivo)
else:
    print("Arquivo não encontrado. Verifique o caminho e tente novamente.")
