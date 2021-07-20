from datetime import *
import requests

url = 'http://192.168.0.13:5000/sync'

timeClient = datetime.now()

formatted = datetime.strftime(timeClient,"%Y-%m-%dT%H:%M:%S.%f")

sync = requests.post(url, json={'key':formatted})

print(sync.text)
