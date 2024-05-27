import os
import cv2
from PIL import Image, ImageTk
import tkinter as tk
from text_to_speech import text_to_speech
import threading
import time

tts = text_to_speech()

# Crear la ventana
main_window = tk.Tk()
main_window.title("Mi primer ventana")
main_window.geometry("800x600")
main_window.resizable(False, False)
main_window.configure(bg="black")

# Crear un label para mostrar el video
label = tk.Label(main_window)
label.place(relx=0.25, rely=0.25, relwidth=0.5, relheight=0.5)

# Cargar el video
path = os.path.dirname(os.path.realpath(__file__)) + "/test.mp4"
video = cv2.VideoCapture(path)

# Variable para controlar si el audio ya ha comenzado
audio_started = False

def speak_with_delay():
  time.sleep(2)
  tts.speak('Hola', 'es')
  time.sleep(1)
  tts.speak('Soy Lucy', 'es')
  time.sleep(0.3)
  tts.speak('y sere tu asistente virtual', 'es')
  time.sleep(0.3)
  tts.speak('En que puedo servirte', 'es')

def show_video():
  global audio_started
  ret, frame = video.read()
  if ret:
    # Convertir el frame a una imagen que pueda mostrarse en Tkinter
    cv2_im = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Obtener el tamaño del widget label
    width = label.winfo_width()
    height = label.winfo_height()

    # Redimensionar la imagen
    cv2_im = cv2.resize(cv2_im, (width, height))

    img = Image.fromarray(cv2_im)
    img_tk = ImageTk.PhotoImage(image=img)
    label.config(image=img_tk)
    label.image = img_tk
    main_window.after(8, show_video)

    # Iniciar el audio después de mostrar el primer frame
    if not audio_started:
      threading.Thread(target=speak_with_delay).start()
      audio_started = True
  else:
    video.release()

# Iniciar la reproducción del video
show_video()

# Ejecutar el mainloop
main_window.mainloop()