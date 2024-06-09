from playsound import playsound
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

text = "My name is atif salam, I am persuing my career in data science"

speak = gTTS(text=text, lang="he", slow=False)

# Using save() method to save the translated
# speech in capture_voice.mp3
speak.save("captured_voice.mp3")

# Using OS module to run the translated voice.
playsound('captured_voice.mp3')
os.remove('captured_voice.mp3')
print(text)
