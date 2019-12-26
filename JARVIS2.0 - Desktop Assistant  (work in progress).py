import pyttsx3
import webbrowser
import smtplib  # sends emails
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
import subprocess
import PyAudio

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('Your_App_ID')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices) - 1].id)  # sets up the voice


def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()


def greetMe():
    currentH = int(datetime.datetime.now().hour)

    if currentH >= 0 and currentH < 12:
        speak('Good morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good afernoon!')

    if currentH >= 18 and currentH != 0:
        speak('Good evening!')


def sayGoodbye():
    currentH = int(datetime.datetime.now().hour)

    if currentH >= 0 and currentH < 12:
        speak('Have a nice morning, Luke!')

    if currentH >= 12 and currentH < 18:
        speak('Have a nice afternoon, Luke!')

    if currentH >= 18 and currentH != 0:
        speak('Have a nice evening, Luke!')


greetMe()

speak("Welcome, Luke! How may I assist you ?")


def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio, language='en-in')
        print('User:' + command + '\n')

    except sr.UnknownValueError:
        speak('Sorry, Luke, I did not got that. Can you please repeat it?')
        command = str(input('Command: '))

    return command


if __name__ == '__main__':

    while True:

        command = myCommand();
        command = command.lower()

        lstMsgs = ['Acknowledged!', 'Working on it!', 'Processing!']

        if 'open youtube' in command:
            speak(random.choice(lstMsgs))
            webbrowser.open('www.youtube.com')

        elif 'open facebook' in command:
            speak(random.choice(lstMsgs))
            webbrowser.open('www.facebook.com')

        elif 'open instagram' in command:
            speak(random.choice(lstMsgs))
            webbrowser.open('www.instagram.com')

        elif 'open google' in command:
            speak(random.choice(lstMsgs))
            webbrowser.open('www.google.com')

        elif 'open gmail' in command:
            speak(random.choice(lstMsgs))
            webbrowser.open('www.gmail.com')

        elif "whats\'s up" in command or 'how are you' in command:
            stMsgs = ['I am up an running and ready for your command!', 'Looking forward in assisting you!']
            speak(random.choice(stMsgs))

        elif 'email' in command:
            speak('Who is the recipient?')
            recipient = myCommand()

            if 'me' in recipient:

                try:
                    speak('What should I say?')
                    content = myCommand()

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", "Recipeint_Username", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry! I am unable to send your message at this moment!')


        elif 'nothing' in command or 'abort' in command or 'stop' in command:
            speak('okay')

        elif 'bye' in command or "No, that is all!" in command:
            speak('See you later, Luke!')
            sys.exit()

        elif 'play music' in command:
            #subprocess.Popen("C:\Users\Luca Petrescu\AppData\Roaming\Spotify")
            speak("Take your pick!")



        else:
            command = command
            speak('Searching...')
            try:
                try:
                    res = client.command(command)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak(results)
                except:
                    results = wikipedia.summary(command, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                speak(results)

            except:
                webbrowser.open('www.google.com')



speak("Do you have anymore commands, Luke?")
