import pyjokes

def tell_joke(*args, **kwargs):
  lang = kwargs.get('lang', 'en')
  cat = kwargs.get('cat', 'neutral')
  return pyjokes.get_joke(language=lang, category=cat) 

if __name__ == "__main__":
  print(tell_joke(lang='es', cat='neutral'))