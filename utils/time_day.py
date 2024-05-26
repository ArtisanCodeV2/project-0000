import datetime

class time_day:
  def __init__(self):
    pass

  def block_time():
    time = datetime.datetime.now().hour

    if time < 12:
      return "mañana"
    elif 12 <= time < 18:
      return "tarde"
    else:
      return "noche"
    
if __name__ == "__main__":
  print(time_day.block_time())