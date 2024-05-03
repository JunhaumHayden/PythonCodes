#pip install gtts
#pip install playsound
#pip instal PyObjC

from gtts import gTTS
from playsound import playsound

audio = 'audio.mp3'
language = 'pt-br'

sp = gTTS(text= 'Fala galera, esse é o meu primeiro audio gerado com IA', lang = language)

sp.save(audio)
playsound(audio)