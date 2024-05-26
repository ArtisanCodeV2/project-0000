import speech_recognition as sr
import unicodedata

class speech_to_text:
  # Esta clase convierte el habla en texto utilizando la API de Google Speech Recognition.
  def __init__(self):
    # Inicializa el reconocedor de voz y el micrófono.
    self.r = sr.Recognizer()
    self.m = sr.Microphone()
    self.r.dynamic_energy_threshold = False

  def listen(self):
    # Escucha el micrófono y convierte el habla en texto.
    # Normaliza el texto antes de devolverlo.
    try:
      with self.m as source:
        self.r.adjust_for_ambient_noise(source)
        audio = self.r.listen(source)
        text = self.r.recognize_google(audio, language='es-ES')
        normalized_text = self.normalize(text)
        return normalized_text
    except sr.UnknownValueError:
      return "No entendí lo que dijiste"
    except sr.RequestError as e:
      return f"Error en la solicitud a Google: {e}"

  @staticmethod
  def normalize( text):
    # Normaliza el texto eliminando los acentos y convirtiendo todo a minúsculas.
    # También maneja el carácter especial 'ñ'.
    cap1 = text.strip().lower()
    cap2 = speech_to_text.spanish_character(cap1, 1)
    cap3 = "".join(c for c in unicodedata.normalize('NFD', cap1) if not unicodedata.combining(c))
    return cap3 if not cap2 else speech_to_text.spanish_character(cap3, 2, cap2)

  @staticmethod
  def spanish_character(text, round, index_changes=None):
    # Maneja el carácter especial 'ñ' en el texto.
    letter = "ñ"
    if round == 1:
      index_letters = [i for i, c in enumerate(text) if c == letter]
      return index_letters
    elif round == 2:
      text_string = list(text)
      for index in index_changes:
        if 0 <= index < len(text_string):
          text_string[index] = letter
      return "".join(text_string)
    
if __name__ == "__main__":
  # Crea una instancia de la clase y prueba la funcionalidad de escucha y normalización.
  s = speech_to_text()
  print(s.listen())
  s.normalize("hola soy un niño")