import tensorflow as tf
import tensorflow_hub as hub
import numpy as np

def embed_useT(module):
    with tf.Graph().as_default():
        sentences = tf.placeholder(tf.string)
        embed = hub.Module(module)
        embeddings = embed(sentences)
        session = tf.train.MonitoredSession()
    return lambda x: session.run(embeddings, {sentences: x})
embed_fn = embed_useT('/home/gourav/Desktop/aries/testbot/model/3(1)')

import speech_recognition as sr 
sample_rate = 48000
#Chunk is like a buffer. It stores 2048 samples (bytes of data) 
#here.  
#it is advisable to use powers of 2 such as 1024 or 2048 
chunk_size = 2048
#Initialize the recognizer 
r = sr.Recognizer() 


from gtts import gTTS
import os
from pygame import mixer 
mixer.init()
mixer.music.load('/home/gourav/Desktop/aries/testbot/good.mp3')

val='e'
f=open("/home/gourav/Desktop/aries/testbot/textfile","r")
score =0
while(True):
    
    x=f.readline()
    if(x[0]=="1"):
        x=f.readline()
        print(x)
        tts = gTTS(x, lang='en')
        tts.save("/home/gourav/Desktop/aries/testbot/good.mp3")
        mixer.music.play()
        #inp=input("enter any key to answer\n")
        with sr.Microphone(device_index = 6, sample_rate = sample_rate,  
                        chunk_size = chunk_size) as source:
            r.adjust_for_ambient_noise(source) 
            print("Say your answer")
    #listens for the user's input 
            audio = r.listen(source)
            text = r.recognize_google(audio)
            #q
            print(text,"voice")
            x=f.readline()
            x.lower()
            print(x,"text")
            messages = [x,text]
            embed_fn(messages)
            encoding_matrix = embed_fn(messages)
            import numpy as np
            arr=np.inner(encoding_matrix, encoding_matrix)
            print(arr)
            score=score+arr[0][1]
            
            
            
            
            val=input("press q to quit,tap enter to go on\n")
            if(val=='q' or val=='Q'):
                f.close
                break  
