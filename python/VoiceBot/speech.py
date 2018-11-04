import speech_recognition as sr
import os
from gtts import gTTS

def listen():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now!")
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        input_speech = r.recognize_google(audio)
        print("You said: " + input_speech)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service")
    return input_speech

def speak(mytext):


    # Language in which you want to convert
    language = 'en'

    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    # have a high speed
    myobj = gTTS(text=mytext, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome
    myobj.save("command.mp3")

    # Playing the converted file
    os.system("mpg321 command.mp3")
