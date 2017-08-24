import petl as etl

table1 = etl.fromjson('Cars.json', header=['Id', 'Name', 'Price'])
print table1