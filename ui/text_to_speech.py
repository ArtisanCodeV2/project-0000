import pyttsx3

class text_to_speech:
  def __init__(self):
    self.voice_map = {
      'es': 3,
      'en': 1
    }

  def speak(self, text, lang):
    engine = pyttsx3.init()

    engine.setProperty('rate', 125)
    engine.setProperty('volume', 1)

    voices = engine.getProperty('voices')
    voice_type = self.voice_map.get(lang, 0)

    try:
      engine.setProperty('voice', voices[voice_type].id)
      engine.say(text)
      engine.runAndWait()
    except Exception as e:
      print(e)
      print("An error occurred while trying to speak.",
        "Contact developer of Lucy")
      
if __name__ == "__main__":
  tts = text_to_speech()
  tts.speak('Hola, soy Lucy', 'es')