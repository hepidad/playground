import requests, json

sumber = "http://hepidad.github.io/data/Cars.json"

data_online = requests.get(sumber)
data_json= json.loads(data_online.content)
data = data_online.json()
print data

for i in range (0,len(data)):
	print data[i]['Id']," ",data[i]['Name']


#print idcars
#print type(Cars)
#data = etl.fromjson("data_online", header=['Id'])
#print data
#d = dict(itertools.izip_longest(*[iter(data_json)] * 2, fillvalue=""))
#print type(data_json)

#data_dumps =  json.dumps(data_json, sort_keys=True, indent=4,separators=(',',':'))
#print repr(data_dumps)
#print type(data_dumps)
#data = json.loads(data_)
#print data
#print type(data)

#idcar = data_json['Id']
#print idcar