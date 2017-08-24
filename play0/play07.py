import petl as etl

table1 = etl.fromxml('Cars.xml','row',['Id','Name','Price'])

#table3 = etl.fromxml('example3.xml', 'row',
#...                      {'foo': 'foo', 'bar': ('baz/bar', 'v')})
print table1