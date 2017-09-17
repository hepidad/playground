import requests, json

sumber = "http://hepidad.github.io/data/Cars.json"

data_online = requests.get(sumber)
data_json = data_online.json()

for i in range(0,len(data_json)):
	print data_json[i]['Id'],data_json[i]['Name'],data_json[i]['Price']