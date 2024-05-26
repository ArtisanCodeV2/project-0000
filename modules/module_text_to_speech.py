import pyttsx3  # Importa el módulo pyttsx3 para la conversión de texto a voz

class TextToSpeechError(Exception):  # Define una excepción personalizada para los errores de TextToSpeech
  pass

class text_to_speech:
  def __init__(self):
    # Mapeo de idiomas a índices de voz. Los índices pueden variar dependiendo del sistema.
    self.voice_map = {
      'es': 3,  # Índice de la voz en español
      'en': 1   # Índice de la voz en inglés
    }
    self.engine = pyttsx3.init()  # Inicializa el motor de voz

    # Configura la velocidad y el volumen de la voz
    self.engine.setProperty('rate', 125)  # Velocidad de la voz
    self.engine.setProperty('volume', 1)  # Volumen de la voz

  def speak(self, text, lang):
    voices = self.engine.getProperty('voices')  # Obtiene las voces disponibles
    voice_type = self.voice_map.get(lang, 0)  # Obtiene el índice de la voz para el idioma dado

    try:
      # Configura la voz y dice el texto
      self.engine.setProperty('voice', voices[voice_type].id)  # Configura la voz
      self.engine.say(text)  # Dice el texto
      self.engine.runAndWait()  # Espera hasta que se haya dicho todo el texto
    except Exception as e:
      # Lanza una excepción personalizada si ocurre un error
      raise TextToSpeechError("An error occurred while trying to speak.") from e

if __name__ == "__main__":
  tts = text_to_speech()  # Crea una instancia de la clase text_to_speech
  try:
    tts.speak('Hola, soy Lucy', 'es')  # Dice "Hola, soy Lucy" en español
  except TextToSpeechError as e:
    # Imprime el mensaje de error si ocurre una excepción TextToSpeechError
    print(str(e), "Contact developer of Lucy")