import nltk
from nltk.corpus import wordnet
import random
import json
import os
import string
from transformers import BertTokenizer, BertForMaskedLM
import torch

nltk.download('wordnet')
nltk.download('omw-1.4')


tokenizer = BertTokenizer.from_pretrained('dccuchile/bert-base-spanish-wwm-uncased')
model = BertForMaskedLM.from_pretrained('dccuchile/bert-base-spanish-wwm-uncased')

# Función para generar sinónimos
def generate_synonyms(word, context_sentence):
  # Reemplaza la palabra en la frase de contexto con el token de máscara
  masked_sentence = context_sentence.replace(word, tokenizer.mask_token)
  # Tokeniza la frase
  input_ids = tokenizer.encode(masked_sentence, return_tensors='pt')
  # Obtiene la posición del token de máscara
  mask_token_index = torch.where(input_ids == tokenizer.mask_token_id)[1]
  # Realiza una predicción con el modelo
  output = model(input_ids, return_dict=True)
  logits = output.logits
  # Obtiene los índices de las palabras más probables
  top_token_ids = torch.topk(logits[0, mask_token_index, :], 10).indices[0]
  # Decodifica los índices de las palabras para obtener los sinónimos
  synonyms = [tokenizer.decode([token_id]) for token_id in top_token_ids]
  # Elimina los signos de puntuación de los sinónimos
  synonyms = [syn.translate(str.maketrans('', '', string.punctuation)) for syn in synonyms]
  return synonyms

# Función para aumentar los datos
def augment_data(data):
    augmented_data = []
    seen_phrases = set()
    for item in data:
        input_phrase = item.get('input')
        output = item.get('output')
        if input_phrase and output:
            words = input_phrase.split()
            for i in range(len(words)):
                synonyms = generate_synonyms(words[i], input_phrase)
                if synonyms:
                    new_word = random.choice(synonyms)
                    new_phrase = ' '.join(words[:i] + [new_word] + words[i+1:])
                    new_phrase = new_phrase.strip()  # Elimina los espacios en blanco al principio y al final
                    if new_phrase not in seen_phrases:
                        augmented_data.append({"input": new_phrase, "output": output})
                        seen_phrases.add(new_phrase)
    return augmented_data

def main():
    # Leer los datos de entrenamiento desde un archivo JSON
    data_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data/language/data_0001.json')
    data_file_output = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data/raw/augmented_data.json')

    # Verifica si el archivo de datos existe
    if not os.path.exists(data_file_path):
      raise FileNotFoundError(f"Data file '{'data/language/data_0001.json'}' not found")

    # Abre el archivo de datos y carga los datos en formato JSON
    with open(data_file_path, 'r', encoding='utf-8') as file:
      data = json.load(file)

    # Generar datos aumentados
    augmented_data = augment_data(data)

    # Escribir los datos aumentados a un archivo JSON
    with open(data_file_output, 'w', encoding='utf-8') as f:
      json.dump(augmented_data, f, indent=2, ensure_ascii=False)

    # Imprimir los datos aumentados
    print(json.dumps(augmented_data, indent=2, ensure_ascii=False))

if __name__ == '__main__':
    main()