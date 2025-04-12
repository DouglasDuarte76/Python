pip install numpy scipy matplotlib

______________

import numpy as np
from scipy.io import wavfile
from scipy.fft import fft, ifft
from scipy.signal import butter, lfilter
import matplotlib.pyplot as plt

______________

# Carregar o arquivo de áudio (formato WAV)
taxa_amostragem, dados = wavfile.read('caminho/para/seu/audio.wav')

# Exibir as primeiras amostras
print(f'Taxa de Amostragem: {taxa_amostragem} Hz')
print(f'Número de Amostras: {len(dados)}')

# Plotar o sinal de áudio
plt.figure(figsize=(10, 4))
plt.plot(dados, color='blue')
plt.title('Sinal de Áudio Original')
plt.xlabel('Amostra')
plt.ylabel('Amplitude')
plt.show()


______________


# Aplicar a Transformada de Fourier
espectro = fft(dados)
frequencias = np.fft.fftfreq(len(espectro), 1/taxa_amostragem)

# Plotar o espectro de frequência
plt.figure(figsize=(10, 4))
plt.plot(frequencias[:len(frequencias)//2], np.abs(espectro[:len(espectro)//2]), color='red')
plt.title('Espectro de Frequência do Sinal de Áudio')
plt.xlabel('Frequência (Hz)')
plt.ylabel('Magnitude')
plt.show()


______________


# Definir o filtro passa-baixa
def butter_lowpass(cutoff, fs, ordem=5):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(ordem, normal_cutoff, btype='low', analog=False)
    return b, a

def filtrar_sinal(data, cutoff, fs, ordem=5):
    b, a = butter_lowpass(cutoff, fs, ordem=ordem)
    y = lfilter(b, a, data)
    return y

# Aplicar o filtro passa-baixa
cutoff_frequencia = 1000.0  # Freqüência de corte em Hz
dados_filtrados = filtrar_sinal(dados, cutoff_frequencia, taxa_amostragem)

# Plotar o sinal de áudio filtrado
plt.figure(figsize=(10, 4))
plt.plot(dados_filtrados, color='green')
plt.title('Sinal de Áudio Filtrado (Passa-Baixa)')
plt.xlabel('Amostra')
plt.ylabel('Amplitude')
plt.show()


______________


wavfile.write('audio_filtrado.wav', taxa_amostragem, dados_filtrados.astype(np.int16))
print('Sinal de áudio filtrado salvo como "audio_filtrado.wav".')
