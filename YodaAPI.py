import requests
headers={
    "X-Mashape-Key": "BoZ5ptmS81mshT78idWKLhTy0ibcp1eV7C1jsnkl5usYYHJN6R",
    "Accept": "text/plain"
  }
translate = input('Learn to speak like me, you will. What would you like to say?: ')
r = requests.get('https://yoda.p.mashape.com/yoda', {'sentence': translate}, headers = headers)
print(r.text)
