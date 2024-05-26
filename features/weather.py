import requests

class tell_weather:
  def __init__(self):
    self.api_key = "5b0250f43e0da2948c48c6793c91249d"
    self.url = "https://api.openweathermap.org/data/2.5/weather?q={},{}&units=metric&appid={}"

  def get_weather(self, *args, **kwargs):
    city = kwargs.get("city") or "Fuenlabrada"
    country = kwargs.get("country") or "ES"

    response = requests.get(self.url.format(city, country, self.api_key))

    if response.status_code == 200:
      data = response.json()
      print(data["main"]["temp"])
      return data["main"]["temp"]
    else:
      return "no logro saber que iempo hace"

if __name__ == "__main__":
  w = tell_weather()
  w.get_weather()