pip install numpy matplotlib

import numpy as np
import matplotlib.pyplot as plt

# Função para simular um LIDAR básico
def gerar_pontos_lidar(num_pontos=100):
    angulos = np.linspace(0, 2 * np.pi, num_pontos)
    raios = 10 + np.random.uniform(-0.5, 0.5, num_pontos)  # Simula pequenas variações naturais
    x = raios * np.cos(angulos)
    y = raios * np.sin(angulos)
    return x, y

# Função para simular um ataque ao LIDAR (inserção de objetos fantasmas)
def ataque_lidar(x, y, num_objetos=3):
    for _ in range(num_objetos):
        angulo = np.random.uniform(0, 2 * np.pi)
        raio_falso = np.random.uniform(5, 15)
        x = np.append(x, raio_falso * np.cos(angulo))
        y = np.append(y, raio_falso * np.sin(angulo))
    return x, y

# Gerar pontos do LIDAR normal
x_normal, y_normal = gerar_pontos_lidar()

# Gerar pontos com ataque (objetos fantasmas)
x_ataque, y_ataque = ataque_lidar(x_normal, y_normal)

# Plotar o LIDAR antes e depois do ataque
fig, ax = plt.subplots(1, 2, figsize=(10, 5))

ax[0].scatter(x_normal, y_normal, c='blue', label="Objetos reais")
ax[0].set_title("Leitura Normal do LIDAR")

ax[1].scatter(x_ataque, y_ataque, c='blue', label="Objetos reais")
ax[1].scatter(x_ataque[-3:], y_ataque[-3:], c='red', marker='x', label="Objetos falsos (ataque)")
ax[1].set_title("Leitura com Ataque de LIDAR")
ax[1].legend()

plt.show()
