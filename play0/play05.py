import requests, json

sumber = "http://hepidad.github.io/data/Cars.json"

data_online = requests.get(sumber)
data_json= json.loads(data_online.content)

print data_json





print type(data_json)