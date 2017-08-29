import requests, json

sumber = "http://localhost:5000/"

data_online = requests.get(sumber)
data = data_online.json()

print data
