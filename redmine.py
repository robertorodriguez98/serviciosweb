import requests
import os
URL_BASE = "https://dit.gonzalonazareno.org/redmine/"
miclave = os.environ['key']
payload = {'key' : miclave}

r=requests.get(URL_BASE+"projects.json"+"?key=",params=payload)
if r.status_code==200:
    doc=r.json()
    for p in doc["projects"]:
        print(str(p["id"])+" "+p["name"])
else:
    print("se ha producido un error")