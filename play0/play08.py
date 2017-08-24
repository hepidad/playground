import xmltodict

with open('Cars.xml') as dream:
    data = xmltodict.parse(dream.read())

print data

