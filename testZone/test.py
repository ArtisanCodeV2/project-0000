from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

class FormFiller:
  def __init__(self, url):
    self.driver = webdriver.Firefox()  # Utiliza el navegador que prefieras
    self.wait = WebDriverWait(self.driver, 10)
    self.driver.get(url)

  def get_form_fields(self):
    soup = BeautifulSoup(self.driver.page_source, 'html.parser')
    form = soup.find('form')
    fields = {}
    for input_element in form.find_all('input'):
      field_name = input_element.get('name')
      field_type = input_element.get('type')
      if field_name and field_type not in ['hidden', 'submit', 'reset', 'button', 'image', 'file']:
        field_input = self.driver.find_element(By.NAME, field_name)
        if field_input.is_displayed():
          if 'user' in field_name or 'email' in field_name or 'login' in field_name:
            fields[field_name] = {'element': field_input, 'type': 'username'}
          elif 'pass' in field_name:
            fields[field_name] = {'element': field_input, 'type': 'password'}
          else:
            fields[field_name] = {'element': field_input, 'type': 'unknown'}
    print(fields)
    return fields

  def fill_field(self, field_label, value):
    fields = self.get_form_fields()
    if field_label in fields:
      field = fields[field_label]
      field.send_keys(value)
    else:
      print(f"No se encontró el campo '{field_label}'")

  def verify_fields(self):
    fields = self.get_form_fields()
    for label, field in fields.items():
      if not field.is_displayed():
        print(f"El campo '{label}' no está visible")
      if not field.is_enabled():
        print(f"El campo '{label}' no está habilitado")

  def close(self):
    self.driver.quit()

if __name__ == "__main__":
  url = "https://api.factorialhr.com/es/users/sign_in?locale=es&return_to=https%3A%2F%2Fapp.factorialhr.com%2F%3Flocale%3Des"
  form_filler = FormFiller(url)
  form_filler.verify_fields()
  form_filler.close()