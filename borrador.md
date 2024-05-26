Módulo module_speech_to_text
Este módulo define una clase speech_to_text que convierte el habla en texto utilizando la API de Google Speech Recognition.

Clase speech_to_text
__init__(self)
Inicializa el reconocedor de voz y el micrófono. No toma ningún argumento.

listen(self)
Escucha el micrófono y convierte el habla en texto. Normaliza el texto antes de devolverlo. No toma ningún argumento.

normalize(self, text)
Normaliza el texto eliminando los acentos y convirtiendo todo a minúsculas. También maneja el carácter especial 'ñ'. Toma un argumento:

text (str): El texto a normalizar.
spanish_character(text, round, index_changes=None)
Método estático. Maneja el carácter especial 'ñ' en el texto. Toma tres argumentos:

text (str): El texto en el que buscar el carácter 'ñ'.
round (int): Indica si se está buscando el carácter 'ñ' (1) o reemplazándolo (2).
index_changes (list, opcional): Una lista de índices donde se encontró el carácter 'ñ' en la primera ronda.
Uso
Crea una instancia de la clase y prueba la funcionalidad de escucha y normalización.