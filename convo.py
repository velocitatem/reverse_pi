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
        rs = get_response(r.recognize_google(audio))
        print(rs[0])
        print(rs[1])

        speak_response(rs[1])

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
