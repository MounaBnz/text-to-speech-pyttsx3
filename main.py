#pip install pyttsx3

import pyttsx3

text_speech = pyttsx3.init()
text_speech.setProperty('rate',150) #the speed is 150 word per minute
while True:
    answer = input("What do you want to convert to speech ? ")
    text_speech.say(answer)
    text_speech.runAndWait()


