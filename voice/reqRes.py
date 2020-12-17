import speech_recognition as sr
import webbrowser
import time
import os
import playsound
from gtts import gTTS
import random


class reqRes():

    def __init__(self):
        self.r = sr.Recognizer()

    

    def get_audio(self, ask = False):
        with sr.Microphone() as source:
            if ask:
                self.billyTalk(ask)
            audio = self.r.listen(source)
            voice_data = ''
            try:
                voice_data = self.r.recognize_google(audio)
            except  sr.UnknownValueError:
                self.billyTalk("Come Again")
            except sr.RequestError:
                self.billyTalk("Network Error")
            return voice_data


    def billyTalk(self, audio_string):
        tts = gTTS(text=audio_string, lang='en')
        r = random.randint(1, 10000000)
        audio_file = 'audio-'+ str(r) + '.mp3'
        tts.save(audio_file)
        playsound.playsound(audio_file)
        print(audio_string)
        os.remove(audio_file)


    def respond(self, voice_data):
        if 'what is your name' in voice_data:
            self.billyTalk("Billy")
        if 'search' in voice_data:
            search = self.get_audio('What do you want to find?')
            url = 'https://google.com/search?q='+search
            webbrowser.get().open(url)
            self.billyTalk("This is what I found for " + search)

