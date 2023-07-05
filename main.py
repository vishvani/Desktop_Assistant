import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia 
import webbrowser
import os
import smtplib

print("Initializing geny")
MASTER="vishu"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#speak func will pronounce  the string ;; to activate speech recognition 'pip install pywin32'
def speak(text):
    engine.say(text)
    engine.runAndWait()

#wish you as per time
def wishMe():
    hour =int( datetime.datetime.now().hour)
    #print(hour)

    if hour>=0 and hour <12 :
        speak("good morning"+MASTER)
    elif hour>=12 and hour<18:
        speak("good afternoon"+MASTER)
    else:
        speak("good Evening"+MASTER)

   # speak("I am geny. how may i help you?")

#take command from microphn to recg ur voice 'pip install pyaudio'
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...") 
        query= r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")

    except Exception as e :
        print("say that again please")
        query=None
    return query

#sending email
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('@gmail.com',pw)
    server.sendmail('@gmail.com',to,content)
    server.close()

def main ():

    # main progm
    speak("Initializing geny...")
    wishMe()
    query = takeCommand()

    #logic for executing tasks as per query
    if 'wikipedia' in query.lower():
        speak("searching wikipedia..")
        query = query.replace('wikipedia',"")
        results = wikipedia.summary(query,sentences=2)
        speak(results)

    elif 'open youtube' in query.lower():
        # webbrowser.open('youtube.com')   #opens in edge
        #url = 'https://www.youtube.com/'
        #chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        #webbrowser.get(chrome_path).open(url)

        chrome_path = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
        url = "http://www.youtube.com/"
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(url)

    elif 'open google' in query.lower():
        chrome_path = r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        url = "http://www.google.com/"
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(url)

    elif 'play music' in query.lower():
        songs_dir="C:\\Users\\vishvani\music"
        songs= os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir,songs[0])) 

    elif 'the time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{MASTER} the time is {strTime}")

    elif 'open code' in query.lower():
        codepath = "C:\\Users\\vishvani\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code"
        os.startfile(codepath)

    elif 'email to' in query.lower():
        try:
            speak("what should i send")
            content = takeCommand()
            to = '@gmail.com'
            sendEmail(to,content)
            speak('email sent')
        except  Exception as e:
            print(e) 

main()