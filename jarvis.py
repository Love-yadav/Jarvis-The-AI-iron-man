import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)



def speak(audio):
 engine.say(audio)
 engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 or hour<12:
        speak("Good Morning sir")
    elif hour>12 or hour<18:
        speak("Good Afternoon sir")
    else:
        speak("Good evening sir")
        
    speak("I am jarvis sir please tell how can i help you:")

def takeCommands():
    # it is take microphone input and then tell us the result about it
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="en-in")
        print(f"User said: {query}")
    except Exception as e:
        # print(e)


        print("Say that again")
        return "None"
    return query




if __name__=='__main__':
    wishMe()
    while True:
    # speak("Hello Mr.stark ! tell me what can i do for you :")
     query=takeCommands().lower()

    # logic for different types of tasks
     if 'wikipedia' in query:
         speak("Searching wikipedia...")
         query=query.replace("wikipedia","")
         result=wikipedia.summary(query,sentences=2)
         speak("according to wikipedia")
         print(result)
         speak(result)
     elif 'open youtube' in query:
         webbrowser.open("youtube.com")
     elif 'open google' in query:
         webbrowser.open("goodle.com")
     elif 'who are you' in query:
         speak(" i am jarvis sir ! and i make your work done")
     elif 'what is time' in query:
         r=datetime.datetime.now().strftime("%H:%M:%S")
         print(r)
         speak(r) 
     elif 'play music' in query:
         music_dir='C:\\Users\\DELL\\Music'
         songs=os.listdir(music_dir)
         print(songs)
         os.startfile(os.path.join(music_dir,songs[4]))
     elif 'open code' in query:
         path="C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
         os.startfile(path)
     elif 'quit' in query:
         exit()