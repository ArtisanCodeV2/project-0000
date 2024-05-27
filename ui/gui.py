# ui.py
import tkinter as tk
from text_to_speech import text_to_speech

tts = text_to_speech()

class GUI:
  def __init__(self):
    # Crear la ventana
    self.main_window = tk.Tk()
    self.main_window.title("Mi primer ventana")
    self.main_window.geometry("800x600")
    self.main_window.resizable(False, False)
    self.main_window.configure(bg="white")

    # Crear los frames para las tres secciones
    self.left_frame = tk.Frame(self.main_window, bg="blue", width=200)
    self.center_frame = tk.Frame(self.main_window, bg="green")
    self.right_frame = tk.Frame(self.main_window, bg="red", width=200)

    # Configurar el grid para que el frame del centro se expanda
    self.main_window.grid_columnconfigure(1, weight=1)
    self.main_window.grid_rowconfigure(0, weight=1)

    # Posicionar los frames
    self.left_frame.grid(row=0, column=0, sticky="ns")
    self.center_frame.grid(row=0, column=1, sticky="nsew")
    self.right_frame.grid(row=0, column=2, sticky="ns")

    # Crear un label para mostrar el video en el frame del centro
    self.label = tk.Label(self.center_frame)
    self.label.pack(expand=True, fill="both")

    # Crear un botón en el frame del centro
    self.button = tk.Button(self.center_frame, text="Botón", command=lambda: print("Botón presionado"))
    self.button.pack()

  def run(self):
    # Ejecutar el mainloop
    self.main_window.mainloop()

if __name__ == "__main__":
  ui = GUI()
  ui.run()