import speech_recognition as sr
import webbrowser
import subprocess
import pyttsx3 
import os
r = sr.Recognizer()
engine = pyttsx3.init() 
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id) 
engine.runAndWait()
print("\n")
engine.say('Hello')
print("You can open...")
print("\n1.GOOGLE CHROME\t2.YOUTUBE\n3.NOTEPAD\t4.SPEAK 'SEARCH FOR ...'\n5.MS EXCEL\t6.NOTEPAD\n7.EXIT\n")
pyttsx3.speak("speak anything...")
with sr.Microphone() as source:
    audio=r.listen(source)
    text=r.recognize_google(audio)
    print("You said: ",format(text))
    p = format(text).upper() 
    if ("GOOGLE" in p) or ("WEB BROWSER" in p) or ("CHROME" in p) or ("BROWSER" in p): 
        pyttsx3.speak("Opening GOOGLE CHROME")
        webbrowser.open('https://www.google.com')

    elif ("YOUTUBE" in p):
        pyttsx3.speak("Opening YOUTUBE")
        webbrowser.open('https://www.youtube.com')

    elif ("NOTE" in p) or ("NOTEPAD" in p) or ("EDITOR" in p): 
        pyttsx3.speak("Opening NOTEPAD")
        os.system("Notepad")

    elif ("SEARCH" in p) or ("FOR" in p) or ("FIND" in p):
        pyttsx3.speak("Opening your requested page")
        url = "https://www.google.com.tr/search?q={}".format(text)
        webbrowser.open_new_tab(url)

    elif ("EXCEL" in p) or ("MSEXCEL" in p) or ("SHEET" in p): 
        pyttsx3.speak("Opening MICROSOFT EXCEL")
        os.system("start EXCEL.EXE")
    
    elif ("EXIT" in p) or ("QUIT" in p) or ("CLOSE" in p): 
        pyttsx3.speak("Exiting")

    else: 
        pyttsx3.speak(p) 
        print("Is Invalid,Please Try Again") 
        pyttsx3.speak("is Invalid,Please try again")