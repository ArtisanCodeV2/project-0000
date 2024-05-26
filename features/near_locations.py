import webbrowser

class tell_location:
  def __init__(self):
    self.mbu = "https://www.google.com/maps/search/{}+{}"
    pass

  def get_places_near_me(self, **kwargs):
    city = kwargs.get("city") or "madrid"
    query = kwargs.get("location") or "parques"
    url_final = self.mbu.format(query, city)
    webbrowser.open(url_final)
    return "Abriendo Google Maps..."
  
if __name__ == "__main__":
  print(tell_location().get_places_near_me(city="navalcarnero", location="100 montaditos")) 