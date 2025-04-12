pip install pyautogui

_____________________________

import pyautogui
import time
import os

_____________________________


# Mover o mouse para uma posição (x, y)
pyautogui.moveTo(100, 200, duration=1)

# Clicar com o botão esquerdo
pyautogui.click()


_____________________________

# Abrir o explorador de arquivos
pyautogui.hotkey('win', 'e')

# Esperar alguns segundos para o explorador abrir
time.sleep(2)

# Navegar para uma pasta específica (digitando o caminho)
pyautogui.write('C:\\Users\\SeuUsuario\\Documents\\', interval=0.1)
pyautogui.press('enter')


_____________________________


origem = 'C:\\Users\\SeuUsuario\\Documents\\Origem\\'
destino = 'C:\\Users\\SeuUsuario\\Documents\\Destino\\'

# Listar arquivos na pasta de origem
arquivos = os.listdir(origem)

# Mover e renomear arquivos
for i, arquivo in enumerate(arquivos):
    novo_nome = f'arquivo_{i+1}.txt'
    os.rename(os.path.join(origem, arquivo), os.path.join(destino, novo_nome))
    print(f'{arquivo} movido e renomeado para {novo_nome}')


_____________________________


# Tirar uma captura de tela
screenshot = pyautogui.screenshot()
screenshot.save('captura_tela.png')

# Localizar um elemento na tela e clicar
localizacao = pyautogui.locateOnScreen('imagem_elemento.png')
if localizacao:
    pyautogui.click(localizacao)

_____________________________



