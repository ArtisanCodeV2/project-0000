try:
  from brain.trainer import trainer
except Exception as e:
  from .brain.trainer import trainer

brain_map = {
  'train': trainer
}

def get_model(model_name):
  return brain_map.get(model_name)