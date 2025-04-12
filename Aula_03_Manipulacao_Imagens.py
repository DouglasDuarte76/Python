from PIL import Image
import matplotlib.pyplot as plt

# Carregar a imagem
imagem = Image.open("caminho/para/sua/imagem.jpg")

# Exibir a imagem
plt.imshow(imagem)
plt.axis('off')  # Ocultar os eixos
plt.show()

# Redimensionar a imagem
imagem_redimensionada = imagem.resize((300, 300))

# Exibir a imagem redimensionada
plt.imshow(imagem_redimensionada)
plt.axis('off')
plt.show()

# Rotacionar a imagem
imagem_rotacionada = imagem.rotate(45)

# Exibir a imagem rotacionada
plt.imshow(imagem_rotacionada)
plt.axis('off')
plt.show()

from PIL import ImageFilter

# Aplicar o filtro de contorno
imagem_contorno = imagem.filter(ImageFilter.CONTOUR)

# Exibir a imagem com contorno
plt.imshow(imagem_contorno)
plt.axis('off')
plt.show()

# Converter para tons de cinza
imagem_cinza = imagem.convert("L")

# Exibir a imagem em tons de cinza
plt.imshow(imagem_cinza, cmap='gray')
plt.axis('off')
plt.show()

# Salvar a imagem redimensionada
imagem_redimensionada.save("imagem_redimensionada.jpg")
