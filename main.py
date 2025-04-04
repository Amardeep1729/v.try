import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
from openai import OpenAI
from gtts import gTTS

import pygame
import os
import random

#pip install PocketSphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "your news api"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

# def speak(text):    
#     tts = gTTS(text)
#     tts.save('temp.mp3')
    

#     #Initialize pygame  mixer   
#     pygame.mixer.init()

#     #load the MP3 file
    
#     pygame.mixer.music.load('temp.mp3')

#     #Play the MP3 file
#     pygame.mixer.music.play()

#     #keep program running until the music stops playing
#     while pygame.mixer.music.get_busy():
#         pygame.time.Clock().tick(10)
#     # not to give any argument in unload
#     pygame.mixer.music.unload()    
#     os.remove   

def aiProcess(command)   :
    client = OpenAI(api_key= "your api key"
    )

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant name jarvis. Give short responses please"},
            {
                "role": "user",
                "content": command      }
  ]
)

    return(completion.choices[0].message.content) 

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" " , 1)[1].strip() #get full song and remove extra space
        link = musiclibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():    
            r = requests.get(f" https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
            data = r.json()

            #print the headlines    
            for article in data.get('articles', []):
                speak_old(article['title'])
    else:
        # Let OpenAI handle the request
        output = aiProcess(c)     
        speak_old(output)       
                



if __name__== "__main__":    
    speak_old("Initializing Jarvissssss.......")
    while True:
        #Listen for the wake word "Jarvis"
        #obtain audio from the microphone

        r = sr.Recognizer()    

        print("recognizing....")   
        try:
            with sr.Microphone() as source:
                print("Listening")
                audio = r.listen(source, timeout=6 , phrase_time_limit=3)
            word = r.recognize_google(audio)    
            if (word.lower() == "jarvis"):
                words = ["how can i help you", "Yaa" , "Hello how can i help you", "Yes ! tell me..", "Yes" , "Hi How was your day"]
                speak_old (random.choice(words))
                #Listen for the command
                with sr.Microphone() as source:
                    print("Jarvis active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


            
        except Exception as e:
            print("Error; {0}".format(e))    
            

            
 