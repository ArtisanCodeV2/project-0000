import speedtest

class tell_network:
  def __init__(self):
    self.st = speedtest.Speedtest(secure=True)
    self.st.get_best_server()

  def get_download_speed(self):
    return self.st.download() / 1024 / 1024
  
  def get_upload_speed(self):
    return self.st.upload() / 1024 / 1024
  
  def get_ping(self):
    return self.st.results.ping
  
  def test_all(self):
    return {
      "download": self.get_download_speed(),
      "upload": self.get_upload_speed(),
      "ping": self.get_ping()
    }
  
if __name__ == "__main__":
  n = tell_network()
  print(n.test_all())