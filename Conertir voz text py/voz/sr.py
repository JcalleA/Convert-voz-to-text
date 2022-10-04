from asyncore import read
from os import path

from pydub import AudioSegment
import speech_recognition as sr
import time
srp=sr.Recognizer()

archivo=open('C:/Users/Calle1413/Downloads/text1.txt','r')
print(archivo.read())


video='prueba30'
formato='.wav'
src = r'C:/Users/Calle1413/Downloads/'+video+'.mp4'
out= r'C:/Users/Calle1413/Downloads/'+video+formato
song = AudioSegment.from_file(src)
song.export(out, format="wav")


with sr.AudioFile('C:/Users/Calle1413/Downloads/'+video+formato) as source:
#with sr.Microphone() as source:
    print('escuchando')
    audio=srp.listen(source)
    try:
        print("leyendo: ")
        text= srp.recognize_google(audio,language="es-ES")
        time.sleep(1.5)
        print(text)
    except: 
        print("no entiendo el audio")

