import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 180-200)

def speak(audio):
        engine.say(audio)
        engine.runAndWait()

speak('Hello, I am Jarvis')
