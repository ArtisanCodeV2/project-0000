import webbrowser

class tell_search:
  def __init__(self):
    pass

  def search(self, topic: str):
    webbrowser.open(f"https://www.google.com/search?q={topic}")

if __name__ == "__main__":
  tell_search().search("python")