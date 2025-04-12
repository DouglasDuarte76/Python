pip install scikit-learn numpy matplotlib

_______________________

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

_______________________

# Carregar o conjunto de dados de dígitos
digits = load_digits()

# Exibir as formas dos dados e das etiquetas
print("Dimensões dos dados:", digits.data.shape)
print("Dimensões das etiquetas:", digits.target.shape)

# Exibir uma amostra de imagens
plt.figure(figsize=(10, 4))
for index, (image, label) in enumerate(zip(digits.data[:5], digits.target[:5])):
    plt.subplot(1, 5, index + 1)
    plt.imshow(image.reshape(8, 8), cmap='gray')
    plt.title(f'Label: {label}')
plt.show()

_______________________

X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.3, random_state=42)


_______________________

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

_______________________


knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

_______________________


y_pred = knn.predict(X_test)

# Matriz de Confusão
print("Matriz de Confusão:")
print(confusion_matrix(y_test, y_pred))

# Relatório de Classificação
print("\nRelatório de Classificação:")
print(classification_report(y_test, y_pred))

_______________________


plt.figure(figsize=(10, 4))
for index, (image, prediction) in enumerate(zip(X_test[:5], y_pred[:5])):
    plt.subplot(1, 5, index + 1)
    plt.imshow(image.reshape(8, 8), cmap='gray')
    plt.title(f'Previsão: {prediction}')
plt.show()
