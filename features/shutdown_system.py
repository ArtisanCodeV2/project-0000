import os
import platform

# Intenta importar el módulo winerror, que contiene códigos de error específicos de Windows.
# Si el módulo no se encuentra (porque no estamos en Windows), simplemente pasa.
try:
  import winerror
except ImportError or ModuleNotFoundError:
  pass

class tell_shutdown:
  def __init__(self):
    # Obtiene el nombre del sistema operativo y lo convierte a minúsculas.
    self.os_name = platform.system().lower()
    # Establece el tiempo de espera antes del apagado a 30 segundos.
    self.time = 30

  def shutdown(self):
    # Si el sistema operativo es Windows...
    if "windows" in self.os_name:
      # Crea el comando para apagar el sistema después de un tiempo de espera.
      cont = f"shutdown -s -t {self.time}"
      # Ejecuta el comando y obtiene el código de error.
      error_code = os.system(cont)
      # Si el código de error indica que ya se ha programado un apagado...
      if winerror is not None and error_code in [winerror.ERROR_SHUTDOWN_IN_PROGRESS, 1115]:
        print("A Shutdown Process has already been Scheduled!")
      else:
        print(f"Your System will Shutdown in {self.time} Seconds!")
    # Si el sistema operativo es Linux...
    elif "linux" in self.os_name:
      # Crea el comando para apagar el sistema después de un tiempo de espera.
      cont = f"shutdown -h {self.time}"
      # Ejecuta el comando.
      os.system(cont)
      print(f"Your System will Shutdown in {self.time} Minutes!")
    # Si el sistema operativo es macOS (Darwin)...
    elif "darwin" in self.os_name:
      # Crea el comando para apagar el sistema después de un tiempo de espera.
      cont = f"shutdown -h -t {self.time}"
      # Ejecuta el comando.
      os.system(cont)
      print(f"Your System will Shutdown in {self.time} Minutes!")
    else:
      # Si el sistema operativo no es ninguno de los anteriores, lanza una advertencia.
      raise Warning(
        f"Available on Windows, Mac and Linux only, can't Execute on {self.os_name}"
      )

  def cancel_shutdown(self):
    # Si el sistema operativo es Windows...
    if "windows" in self.os_name:
      # Ejecuta el comando para cancelar el apagado y obtiene el código de error.
      error_code = os.system("shutdown /a")
      # Si el código de error indica que no se ha programado ningún apagado...
      if error_code == winerror.ERROR_NO_SHUTDOWN_IN_PROGRESS:
        print(
          "Shutdown Cancellation process has been Aborted! [NO Shutdown Scheduled]"
        )
      else:
        print("Shutdown has been Cancelled!")
    # Si el sistema operativo es Linux...
    elif "linux" in self.os_name:
      # Ejecuta el comando para cancelar el apagado.
      os.system("shutdown -c")
      print("Shutdown has been Cancelled!")
    # Si el sistema operativo es macOS (Darwin)...
    elif "darwin" in self.os_name:
      # Ejecuta el comando para cancelar el apagado.
      os.system("killall shutdown")
      print("Shutdown has been Cancelled!")

if __name__ == "__main__":
  from time import sleep
  # Crea una instancia de tell_shutdown y programa un apagado.
  tell_shutdown().shutdown()
  # Espera 10 segundos.
  sleep(10)
  # Cancela el apagado.
  tell_shutdown().cancel_shutdown()