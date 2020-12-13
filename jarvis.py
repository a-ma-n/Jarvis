import wikipedia
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
import smtplib

engine =pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<=18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir Your virtual assistant. Please tell me how may I help you ")


def takeCommand():
    # It takes microphone input from the user and return string output

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1#use control + click to get info about pause_threshold
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query =r.recognize_google(audio, language='en-in') 
        print(f"User said {query}\n")

    except Exception as e:
        #print(e)
        print('Say that again please....')
        return "None"#not the python None we return a string here 
    return query
#energy threshold increase like to speak louder if theres noise in your area 
'''
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()

    server.sendmail('aman.la.mart@gmail.com',to ,content)
    server.close()
'''
if __name__ == "__main__":

 #   speak("seemeen's collection")
    wishMe() 
    while True:
        query = takeCommand().lower()
    #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results= wikipedia.summary(query, sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir = 'D:\\Ai\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[6]))#can also use random module from 0 to l-1
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        elif 'open code' in query:
            codePath = "C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        '''
        elif 'send email to aman' in query:
            try:
                speak('What should i say')
                content = takeCommand()
                to = "aman.la.mart@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry my friend Aman bhai.I am not able to send the email")
                '''
        elif 'exit' in query:
                 exit(1)
        elif 'camera' in query:
            import camera_timer
            



