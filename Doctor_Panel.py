import speech_recognition as sr
import pyttsx3
from tkinter import *












def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        var1.set("Listening.....")
        window.update()
        print("Listening.....")
        r.pause_threshold = 1
         
        audio = r.listen(source)
    try:
        var1.set("Recoginizers...")
        window.update()
        print("Recoginizers.....")
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say it again please sir")
        return "None"
    var1.set(query)
    window.update()
    return query
