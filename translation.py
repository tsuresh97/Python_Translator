from googletrans import Translator  # Import Translator module from googletrans package
import goslate
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
#quiet the endless 'insecurerequest' warning
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from pygame import mixer
mixer.init()
translator = Translator() # Create object of Translator.

while (True == True):
# obtain audio from the microphone
  r = sr.Recognizer()
  with sr.Microphone() as source:
    #print("Please wait. Calibrating microphone...")
    # listen for 1 second and create the ambient noise energy level
    r.adjust_for_ambient_noise(source, duration=1)
    print("Say Something!!!")
    audio = r.listen(source,phrase_time_limit=5)
 # recognize speech using Sphinx/Google
  try:
      response = r.recognize_google(audio,language="en")  
      print("You said: '" + response + "'")
      tts = gTTS(text="I think you said "+str(response), lang="ta")
      #change ta to your language
      tts.save("response.mp3")
      playsound("response.mp3")
  except sr.UnknownValueError:
          print("Sphinx could not understand audio")
  except sr.RequestError as e:
      print("Sphinx error; {0}".format(e))
