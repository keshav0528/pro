import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os
import wikipedia

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
 
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>=12 and hour <=18:
        speak("good afternoon")
    else:
         
        speak("good evening")

    speak("hello i am jarvis how may i help you keshav sir ")

def takecommand():
    #its take command

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio,language='en-in')
        print("user said: ",query)

    except Exception as e:
        #print(e)    
        print("Say that again please...")    
        return "None" 
    return query
    

if __name__ == "__main__":
    wishme()
    while True:

        query=takecommand().lower()


        if 'wikipedia' in query:
            print("seaching  wikipedia......")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            print(results)
            speak(results)
        

        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com") 
        
           