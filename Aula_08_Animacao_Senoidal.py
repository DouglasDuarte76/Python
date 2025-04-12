import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Configurar a figura e os eixos
fig, ax = plt.subplots()
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1, 1)

# Criar uma linha vazia que será atualizada na animação
linha, = ax.plot([], [], lw=2)

# Função de inicialização
def init():
    linha.set_data([], [])
    return linha,

# Função de atualização
def atualizar(frame):
    x = np.linspace(0, 2 * np.pi, 1000)
    y = np.sin(x + 0.1 * frame)
    linha.set_data(x, y)
    return linha,

# Criar a animação
animacao = FuncAnimation(fig, atualizar, frames=100, init_func=init, blit=True)

# Exibir a animação
plt.show()

# Salvar a animação em um arquivo de vídeo
animacao.save("animacao_senoidal.mp4", writer='ffmpeg')
