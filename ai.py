import pyttsx3
import datetime
import speech_recognition as speechreg
import pyaudio
import wikipedia
import webbrowser
import os

engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    time= int(datetime.datetime.now().hour)
    if time>=0 and time<12:
        speak("Good Morning Sir!")
    elif time>=12 and time<16:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    
    speak("Hi I am Skynet. Your virtual assistant. How can I help you")

def takecomd():
    #microphone input and return string output
    r= speechreg.Recognizer()
    with speechreg.Microphone() as source:
        print("Listening.......")
        r.pause_threshold= 1
        audio= r.listen(source)
    try:
        print("Recognizing......")
        query= r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception:
        print("Kindly Repeat...")
        return "None"
    return query
    
    
if __name__=="__main__":
    wish()
    while True:
        query= takecomd().lower()

        if 'wikipedia' in query:
            speak("Searching From Wikipedia...")
            query= query.replace("wikipedia", "")
            results= wikipedia.summary(query, sentences=5)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'play music' in query:
            webbrowser.open("music.amazon.in")
        elif 'time' in query:
            strTime= datetime.datetime.now().strftime("%H hours %M minutes %S seconds")
            print(f"Sir the time is{strTime}")
            speak(f"Sir the time is{strTime}")
        elif 'open spotify' in query:
            path="C:\\Users\\Lenovo\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(path)
        elif 'open brave' in query:
            path1="C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(path1)
        elif 'open word' in query:
            path2="C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(path2)        
        elif 'open excel' in query:
            path3="C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(path3)            
        elif 'open powerpoint' in query:
            path4="C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE"
            os.startfile(path4)
        elif 'open epic games' in query:
            path5="D:\\Sarthak\\Epic Games\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe"
            os.startfile(path5)
        
        
    
    
    
