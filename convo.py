from main import get_response
from main import speak_response
import speech_recognition as sr
r = sr.Recognizer()

# create a continuous loop to listen for audio and convert it to text
while True:
    with sr.Microphone() as source:
        print("Say something!")
        # set a threshold value for ambient noise
        # continue when stops talking
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        print("Google Speech Recognition thinks you said:")
        print(r.recognize_google(audio))
        (response_texts, response_sid) = get_response(r.recognize_google(audio))
        print(response_texts)
        print(response_sid)

        if response_sid:
            speak_response(response_sid)

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
