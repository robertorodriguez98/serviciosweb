import requests
import os
URL_BASE = "https://dit.gonzalonazareno.org/redmine/"
miclave = os.environ['key']
payload = {'key' : miclave}

r=requests.get(URL_BASE+"projects.json"+"?key=",params=payload)

