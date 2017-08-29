import requests, json

#sumber = "http://hepidad.github.io/data/Cars.json"

data_online = requests.get(sumber)
data = data_online.json()
data_json= json.loads(data_online.content)

print data_json
print type(data_json)
print data_json[3]['Name']
print "===="
data = data_online.json()
print data 
print type(data)
print data[3]['Name']
#for i in range (0,len(data)):
#	print data[i]['Id']," ",data[i]['Name']


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