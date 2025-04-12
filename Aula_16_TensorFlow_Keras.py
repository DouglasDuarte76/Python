pip install tensorflow

_________________

import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt

_________________

# Carregar o conjunto de dados MNIST
(X_train, y_train), (X_test, y_test) = datasets.mnist.load_data()

# Normalizar os dados para o intervalo [0, 1]
X_train, X_test = X_train / 255.0, X_test / 255.0

# Redimensionar os dados para incluir o canal de cor (necessário para CNN)
X_train = X_train.reshape((X_train.shape[0], 28, 28, 1))
X_test = X_test.reshape((X_test.shape[0], 28, 28, 1))

_________________

model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Compilar o modelo
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])


_________________

history = model.fit(X_train, y_train, epochs=5, 
                    validation_data=(X_test, y_test))

_________________

test_loss, test_acc = model.evaluate(X_test, y_test, verbose=2)
print(f'\nAcurácia no conjunto de teste: {test_acc:.2f}')

_________________

# Plotar a acurácia e a perda durante o treinamento
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Acurácia de Treinamento')
plt.plot(history.history['val_accuracy'], label='Acurácia de Validação')
plt.xlabel('Época')
plt.ylabel('Acurácia')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Perda de Treinamento')
plt.plot(history.history['val_loss'], label='Perda de Validação')
plt.xlabel('Época')
plt.ylabel('Perda')
plt.legend()

plt.show()

_________________


# Prever para imagens individuais
predictions = model.predict(X_test[:5])

plt.figure(figsize=(10, 4))
for i in range(5):
    plt.subplot(1, 5, i + 1)
    plt.imshow(X_test[i].reshape(28, 28), cmap='gray')
    plt.title(f'Previsão: {predictions[i].argmax()}')
plt.show()



