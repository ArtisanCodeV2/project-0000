try:
  from utils.text_to_speech import text_to_speech
  from utils.speech_to_text import speech_to_text
  from utils.time_day import time_day
  from utils.interpreter import interpreter
except Exception as e:
  from .utils.text_to_speech import text_to_speech
  from .utils.speech_to_text import speech_to_text
  from .utils.time_day import time_day
  from .utils.interpreter import interpreter

utils_map = {
  'speak': text_to_speech,
  'listen': speech_to_text,
  'time': time_day,
  'interpreter': interpreter
}

def get_util(util_name):
  return utils_map.get(util_name)