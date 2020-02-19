with sr.Microphone(device_index = 6, sample_rate = sample_rate,  
                        chunk_size = chunk_size) as source: 
    r.adjust_for_ambient_noise(source) 
    print("Say Something")
    #listens for the user's input 
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)
