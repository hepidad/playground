import json

data = json.loads(open('Cars.json').read())
print data
print type(data)
