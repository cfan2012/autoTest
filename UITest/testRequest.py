
import os
import requests



path = os.getcwd();
path = 'https://diqa.api.thoughtworks.net/planets/xbtest-1'
r = requests.head('https://diqa.api.thoughtworks.net', data = {'Content-Type':'application/json'})
r = requests.get(path)
print(r.text)
print(r.headers)