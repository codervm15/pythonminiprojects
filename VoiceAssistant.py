# Here we create an AI assistant named ALEX

import pyttsx3  # Python text to speech module
import datetime  # Python Date and time module
import speech_recognition as sr  # Python module for voice input from user
from time import sleep

import webbrowser   #Python module to deal with web browser tasks



engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def takeCommand():
    """
    This function will take input voice command from user
    using microphone and return that command as string.
    """

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        value=query.lower()
        #print(f"User Said: {value}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"

    return value


def speak(audio):
    """
    This function will speak tha data provided as audio
    """

    engine.say(audio)
    engine.runAndWait()


def wishme():
    """
    This function will wish user by calculating time
    """

    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        speak("Good Morning!")

    elif 12 <= hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Hi, I am Alex Sir. Please tell me How may I help you?")



if __name__ == "__main__":
    """
    This is tha main function will call the desired 
    function and perform all the tasks
    """

    wishme()

    while True:
        query = takeCommand()


        if 'open google' in query:
            webbrowser.open("https://www.google.com")

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'hack nasa' in query:
            print('It is difficult sir, but I will try my best....')
            sleep(3)
            print("Initializing attack on their servers, sir....")
            sleep(3)
            print("Attacking their servers, sir ")
            sleep(3)
            print('10% done')
            sleep(3)
            print('40% done')
            sleep(3)
            print('60% done')
            sleep(3)
            print('100% done')
            sleep(3)
            print('We are inside their server sir....')
            sleep(1)
            print('What next sir ?')

        elif 'stop' in query:
            speak("OK sir, I am Quitting, Bye")
            exit()
