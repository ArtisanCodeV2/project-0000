import joblib
import json
import random

class interpreter:
  def __init__(self):
    self.mtPredict = joblib.load("lucy/brain/models/neural_language.pkl")
    with open("lucy/brain/data/answers/answers_0000.json", 'r', encoding='utf-8') as file:
      self.response = json.load(file)

  def interpreter_choice(self, message):
    prediction = self.mtPredict.predict([ message ])
    match prediction:
      case 'saludar':
        return random.choice(self.response['saludar'])
      case 'despedir':
        return random.choice(self.response['despedir'])
      case 'feature/red':
        print('feature/red')
        get_action('network').test_all()