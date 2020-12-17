import speech_recognition as sr
import webbrowser
import time
import os
import playsound
from gtts import gTTS
import random

r = sr.Recognizer()

def get_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            billyTalk(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except  sr.UnknownValueError:
            billyTalk("Come Again")
        except sr.RequestError:
            billyTalk("Network Error")
        return voice_data


def billyTalk(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-'+ str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(voice_data):
    if 'what is your name' in voice_data:
        billyTalk("Billy")
    if 'search' in voice_data:
        search = get_audio('What do you want to find?')
        url = 'https://google.com/search?q='+search
        webbrowser.get().open(url)
        billyTalk("This is what I found for " + search)


time.sleep(1)
billyTalk("How can I help you!")
while 1:
    voice_data = get_audio()
    respond(voice_data)