import pyttsx3
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)
# using male voice


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    # it takes microphone input from user
    pass


def wishme():
    hour = int(datetime.datetime.now().hour)
    if 2 < hour <= 12:
        speak("Good Morning")
    elif 12 < hour <= 17:
        speak("Good Afternoon")
    else:
        speak("Good Evening")





if __name__ == '__main__':
    wishme()
    speak("hi my name is Vox")
