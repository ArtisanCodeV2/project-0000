# Importa las bibliotecas necesarias
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import json
import os

# Define la clase TrainerNeuralLanguage
class TrainerNeuralLanguage:
  def __init__(self):
    # Obtiene el directorio raíz del archivo actual
    self.root_dir = os.path.dirname(os.path.realpath(__file__))

  def train_basic(self, data_file: str = 'data/language/data_0001.json', test_size: float = 0.1, accuracy_threshold: float = 0.7) -> str:
    # Construye la ruta completa al archivo de datos
    data_file_path = os.path.join(self.root_dir, data_file)

    # Verifica si el archivo de datos existe
    if not os.path.exists(data_file_path):
      raise FileNotFoundError(f"Data file '{data_file}' not found")

    # Abre el archivo de datos y carga los datos en formato JSON
    with open(data_file_path, 'r', encoding='utf-8') as file:
      data = json.load(file)

    # Extrae las conversaciones de los datos
    conversations = [(dato['input'], dato['output']) for dato in data]
    texts, labels = zip(*conversations)

    # Divide los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=test_size, random_state=42)

    # Define el pipeline de entrenamiento
    pipeline = Pipeline([
      ('vectorizer', CountVectorizer()),  # Vectoriza los textos
      ('classifier', MultinomialNB())  # Clasificador Naive Bayes multinomial
    ])

    # Entrena el modelo
    pipeline.fit(X_train, y_train)

    # Predice las etiquetas para el conjunto de prueba
    y_pred = pipeline.predict(X_test)

    # Calcula la precisión del modelo
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy: {accuracy:.3f}')

    # Si la precisión es mayor que el umbral, guarda el modelo
    if accuracy > accuracy_threshold:
      model_file_path = os.path.join(self.root_dir, 'models/neural_language.pkl')
      joblib.dump(pipeline, model_file_path)
      return 'Model saved successfully'
    else:
      return 'Model accuracy is too low'

# Si el script se ejecuta como el principal, entrena el modelo
if __name__ == "__main__":
  trainer = TrainerNeuralLanguage()
  trainer.train_basic('data/language/data_0001.json', 0.2, 0.6)