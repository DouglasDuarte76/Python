pip install tensorflow keras numpy matplotlib foolbox

import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

# Carregar dataset MNIST (dígitos manuscritos)
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Normalizar e redimensionar os dados
x_train, x_test = x_train / 255.0, x_test / 255.0
x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)

# Criar modelo de rede neural convolucional
modelo = keras.Sequential([
    keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    keras.layers.MaxPooling2D(2, 2),
    keras.layers.Flatten(),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

# Compilar e treinar o modelo
modelo.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
modelo.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))

# Testar modelo original
test_loss, test_acc = modelo.evaluate(x_test, y_test, verbose=2)
print(f"\nAcurácia do Modelo Original: {test_acc:.2%}")

_________________________________________________________________________________________

import foolbox as fb
import torch

# Converter modelo para formato compatível com Foolbox
fmodel = fb.TensorFlowModel(modelo, bounds=(0, 1))

# Escolher uma imagem para o ataque
imagem = x_test[0:1]
rotulo_real = y_test[0]

# Criar ataque adversarial FGSM
ataque = fb.attacks.FGSM()
imagem_adversarial, sucesso = ataque(fmodel, torch.tensor(imagem), criterion=rotulo_real, epsilons=0.1)

# Exibir imagens antes e depois do ataque
fig, ax = plt.subplots(1, 2, figsize=(8, 4))
ax[0].imshow(imagem[0].squeeze(), cmap="gray")
ax[0].set_title("Imagem Original")

ax[1].imshow(imagem_adversarial.squeeze().detach().numpy(), cmap="gray")
ax[1].set_title("Imagem Adversarial")

plt.show()

# Verificar a nova predição do modelo
predicao = modelo.predict(imagem_adversarial.detach().numpy())
print(f"Rótulo Original: {rotulo_real}, Predição do Modelo Após Ataque: {np.argmax(predicao)}")
