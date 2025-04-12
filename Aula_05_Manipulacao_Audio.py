pip install pydub

from pydub import AudioSegment

# Carregar o arquivo de áudio
audio = AudioSegment.from_file("caminho/para/seu/audio.mp3")

# Salvar uma cópia do arquivo de áudio
audio.export("audio_copia.mp3", format="mp3")

# Aumentar a velocidade do áudio em 1.5x
audio_rapido = audio.speedup(playback_speed=1.5)

# Salvar o áudio alterado
audio_rapido.export("audio_rapido.mp3", format="mp3")


# Aumentar o volume do áudio em 6 dB
audio_alto = audio + 6

# Diminuir o volume do áudio em 6 dB
audio_baixo = audio - 6

# Salvar os áudios alterados
audio_alto.export("audio_alto.mp3", format="mp3")
audio_baixo.export("audio_baixo.mp3", format="mp3")

# Reverter o áudio
audio_reverso = audio.reverse()

# Salvar o áudio reverso
audio_reverso.export("audio_reverso.mp3", format="mp3")


# Carregar outro arquivo de áudio
outro_audio = AudioSegment.from_file("caminho/para/outro/audio.mp3")

# Mixar os dois áudios
mix_audio = audio.overlay(outro_audio)

# Salvar o áudio mixado
mix_audio.export("audio_mix.mp3", format="mp3")


