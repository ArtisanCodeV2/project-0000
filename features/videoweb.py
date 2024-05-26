import webbrowser
import requests

class tell_videoweb:
  def __init__(self):
    self.url = "https://www.youtube.com/results?search_query="
    self.url2 = "https://www.youtube.com{}"

  def handler_videoweb(self, topic, open_video: bool = True):
    url_complete = self.url + topic
    count = 0
    cont = requests.get(url_complete, timeout=5)
    data = str(cont.content)
    list_data = data.split('"')

    for i in list_data:
      count += 1
      if i == "WEB_PAGE_TYPE_WATCH":
        break
    
    if list_data[count-5] == "/results":
      return "Lo siento, no pude encontrar nada sobre " + topic
    
    if  open_video:
      webbrowser.open(self.url2.format(list_data[count-5]))

    return self.url2.format(list_data[count-5])

if __name__ == "__main__":
    tell_videoweb().handler_videoweb("ramstein deutschland", True)

