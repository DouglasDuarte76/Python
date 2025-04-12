pip install moviepy

from moviepy.editor import *

# Carregar imagens
imagem1 = ImageClip("caminho/para/imagem1.jpg").set_duration(2)
imagem2 = ImageClip("caminho/para/imagem2.jpg").set_duration(2)
imagem3 = ImageClip("caminho/para/imagem3.jpg").set_duration(2)

# Carregar áudio
audio = AudioFileClip("caminho/para/audio.mp3")

# Criar um vídeo a partir das imagens
video = concatenate_videoclips([imagem1, imagem2, imagem3], method="compose")

# Adicionar áudio ao vídeo
video = video.set_audio(audio)

# Adicionar texto sobreposto
texto = TextClip("Projeto Multimídia", fontsize=70, color='white')
texto = texto.set_position('center').set_duration(6)
video = CompositeVideoClip([video, texto])

# Exportar o vídeo final
video.write_videofile("video_final.mp4", codec="libx264", audio_codec="aac")

