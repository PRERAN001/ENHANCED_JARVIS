import pyttsx3
engine = pyttsx3.init()
def txt_to_speak(queery):
    engine.say(queery)
    engine.runAndWait()

