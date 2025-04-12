pip install opencv-python

___________________


import cv2
import matplotlib.pyplot as plt

___________________

# Carregar a imagem
imagem = cv2.imread('caminho/para/sua/imagem.jpg')

# Converter a imagem para RGB (padrão do Matplotlib)
imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

# Exibir a imagem
plt.imshow(imagem_rgb)
plt.axis('off')  # Ocultar os eixos
plt.show()

___________________

# Converter para escala de cinza
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Exibir a imagem em tons de cinza
plt.imshow(imagem_cinza, cmap='gray')
plt.axis('off')
plt.show()

___________________


# Aplicar detecção de bordas usando Canny
bordas = cv2.Canny(imagem_cinza, 100, 200)

# Exibir a imagem com bordas detectadas
plt.imshow(bordas, cmap='gray')
plt.axis('off')
plt.show()

___________________

# Carregar o classificador Haar Cascade para detecção de rostos
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Detectar rostos na imagem
rostos = face_cascade.detectMultiScale(imagem_cinza, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Desenhar retângulos ao redor dos rostos detectados
for (x, y, w, h) in rostos:
    cv2.rectangle(imagem_rgb, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Exibir a imagem com os rostos detectados
plt.imshow(imagem_rgb)
plt.axis('off')
plt.show()

___________________


# Converter de volta para BGR para salvar corretamente
imagem_bgr = cv2.cvtColor(imagem_rgb, cv2.COLOR_RGB2BGR)

# Salvar a imagem processada
cv2.imwrite('imagem_com_rostos_detectados.jpg', imagem_bgr)


