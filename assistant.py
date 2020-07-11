# pyttsx3 is speech to text python library which also works offline
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

# sapi is microsoft api used for speech recognition and speech synthesis in windows applications
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour > 12 and hour < 16:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am cauwa, How May I help You")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold=200
        print("n")
        audio = r.listen(source)
        print('hello')

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query 




if __name__ == "__main__":
    wishme()
    while True:
        query=takeCommand().lower()

        if 'wikipedia' in query:
            speak("searching wikipedia..")
            query=query.replace('wikipedia','')
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'youtube' in query:
            webbrowser.open('www.youtube.com')

        elif 'github' in query:
            webbrowser.open('www.github.com')   

        elif 'stack overflow' in query:
            webbrowser.open('www.stackoverflow.com')

        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(strTime)    
        
        elif 'code' in query:
            path="C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        elif 'quit' in query:
            quit()