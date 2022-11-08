import pyttsx3

# def speak(word):
#     speak = pyttsx3.init()
#     speak.say(word)
#     speak.runAndWait()
#     speak.stop()
#
# speak(1561343)

with open("test.txt", "r", encoding="utf-8") as f:
    file = f.read()
    speak = pyttsx3.init()
    speak.say(file)
    speak.runAndWait()
    speak.stop()
