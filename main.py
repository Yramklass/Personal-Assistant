
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice','voices[1].id') # 0 for male, 1 for female

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello, good morning.")
        print ("Hello, good morning.")
    elif hour>12 and hour<18:
        speak("Hello, good afternoon.")
        print ("Hello, good afternoon.")
    else:
        speak ("Hello, good evening.")
        print ("Hello, good evening.")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ("Listening...")
        audio = r.listen(source)
        
        try:
            statement = r.recognize_google(audio, language='en-uk') #works??
            print (f"User said:{statement}\n")
        except Exception as e:
            speak("Pardon me, please say that again.")
            return "None"
        return statement
    

'''print ("Loading your AI personal assistant.")
speak ("Loading your AI personal assistant.")
wishMe'''


if __name__=='__main__':
    while True:
        speak("How can I help?")
        print ("How can I help?")
        statement = takeCommand().lower()
        if statement == 0:
            continue 

        if 'bye' in statement or 'goodbye' in statement:
            speak("Shutting Down.")
            print("Shutting Down.")
            break
        elif 'wikipedia' in statement:
            speak("Searching Wikipedia...")
            print("Searching Wikipedia...")
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement,sentences= 3)
            speak ("According to Wikipedia ")
            print ("According to Wikipedia ")
            speak(results)
            print(results)
        elif 'open youtube' in statement:
            webbrowser.Chrome.open_new_tab("https://youtube.com")
            time.sleep(5)
        elif 'open google' in statement:
            webbrowser.Chrome.open_new_tab("https://google.com")
            time.sleep(5)    
        elif 'open gmail' in statement:
            webbrowser.Chrome.open_new_tab("gmail.com")    
            time.sleep(5)
        
        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0,"robo camera","img.jpg")
        
        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.Chrome.open_new_tab(statement)
            time.sleep(5)
        
        
        







    