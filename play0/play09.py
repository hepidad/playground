import requests

sumber = "http://hepidad.github.io/data/Cars.xml"
headers = {'accept': 'application/xml;'}

data_online = requests.get(sumber, headers=headers)

print data_online.text



