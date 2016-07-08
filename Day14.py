import requests

text = input("Enter string here.")
r = requests.post('http://api.phteven.io/translate/', {"text": text})

resp = r.json()
print(resp['data'])
# print(r.text)
