import speech_recognition as sr
import unicodedata

class speech_to_text:
  def __init__(self):
    self.r = sr.Recognizer()
    self.m = sr.Microphone()
    self.r.dynamic_energy_threshold = False

  def listen(self):
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
  def normalize(text):
    cap1 = text.strip().lower()
    cap2 = speech_to_text.spanish_character(cap1, 1)
    cap3 = "".join(c for c in unicodedata.normalize('NFD', cap1) if not unicodedata.combining(c))
    return cap3 if not cap2 else speech_to_text.spanish_character(cap3, 2, cap2)

  @staticmethod
  def spanish_character(text, round, index_changes=None):
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
  s = speech_to_text()
  print(s.listen())