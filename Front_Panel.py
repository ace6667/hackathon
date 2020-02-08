from tkinter import *
import speech_recognition as sr
import pyttsx3
import os
import threading
import datetime
import pymysql


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)






window = Tk()
window.geometry("390x590+500+50")
window.title('Main panel')
window.configure(background="floralwhite")
photo = PhotoImage(file="C:/Users/Jerry/Pictures/Assistant.gif")

myLabel1 = Label(image=photo,width = 400,height=400,bg='floralwhite',fg="floralwhite")
myLabel1.pack()
myLabel1.place(x=0,y=0)

mylabel_name = Label(text="Dr.Shree",font="Sans-Serif 10 bold",bg="Pink",fg="Purple")
mylabel_name.pack()
mylabel_name.place(x=0,y=5,width=100)

global var1
var1 = StringVar()

bar = Label(textvar=var1,font="Monospace 10 ",bg="Pink",fg="red")
bar.pack()
bar.place(x=0,y=550,width=390,height=40)
    
    



def speak(audio):
    engine.say(audio)
    
    engine.runAndWait()    




def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        var1.set("Good Morning ")
        window.update()
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        var1.set("Good Afternoon  ")
        window.update()
        speak("Good Afternoon")
    else:
        var1.set("Good Evening ")
        window.update()
        speak("Good Evening")
        speak("I'm      ALexa  ")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:

       
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
       
        print("Recoginizers.....")
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say it again please sir")
        return "None"
       
    return query




if __name__ == "__main__":
    wishMe()

    
   
    if True:
        query = takeCommand().lower()
        
        if 'Search for Doctor' in query:
            speak("OK Sir")
            speak("Which ")


window.mainloop()

