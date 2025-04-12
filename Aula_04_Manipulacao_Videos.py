import cv2

# Inicializar a captura de vídeo
captura = cv2.VideoCapture(0)

while True:
    # Capturar frame a frame
    ret, frame = captura.read()

    # Exibir o frame
    cv2.imshow('Video', frame)

    # Pressionar 'q' para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar a captura e fechar as janelas
captura.release()
cv2.destroyAllWindows()


captura = cv2.VideoCapture(0)

while True:
    ret, frame = captura.read()
    # Converter para tons de cinza
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Video em Tons de Cinza', gray_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

captura.release()
cv2.destroyAllWindows()


captura = cv2.VideoCapture(0)

while True:
    ret, frame = captura.read()
    # Aplicar filtro Canny
    edges = cv2.Canny(frame, 100, 200)

    cv2.imshow('Detecção de Bordas', edges)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

captura.release()
cv2.destroyAllWindows()


captura = cv2.VideoCapture(0)
largura = int(captura.get(cv2.CAP_PROP_FRAME_WIDTH))
altura = int(captura.get(cv2.CAP_PROP_FRAME_HEIGHT))
tamanho = (largura, altura)

# Definir o codec e criar o objeto VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'XVID')
saida = cv2.VideoWriter('video_processado.avi', fourcc, 20.0, tamanho)

while True:
    ret, frame = captura.read()
    if not ret:
        break

    # Converter para tons de cinza
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Converter de volta para BGR para salvar corretamente
    gray_frame_bgr = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2BGR)

    # Escrever o frame processado no vídeo de saída
    saida.write(gray_frame_bgr)

    cv2.imshow('Video em Tons de Cinza', gray_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

captura.release()
saida.release()
cv2.destroyAllWindows()

