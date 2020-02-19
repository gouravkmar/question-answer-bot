from gtts import gTTS
import os
from pygame import mixer 
mixer.init()
tts = gTTS(text='Good morning how are you,well', lang='en')
tts.save('/home/gourav/Desktop/aries/testbot/good.mp3')

mixer.music.load("/home/gourav/Desktop/aries/testbot/good.mp3")

mixer.music.play()
