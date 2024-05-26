from neural_language import trainer_neural_language
import os

class trainer:
  def __init__(self):
    pass

  def neural_trainer_choice(self, type_data):
    switcher = {
      'neural_language': trainer_neural_language()
    }

    return switcher.get(type_data, 'Invalid type data')

if __name__ == "__main__":
  t = trainer()
  t.neural_trainer_choice('neural_language').train_basic()