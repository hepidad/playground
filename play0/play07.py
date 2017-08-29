import petl as etl

table1 = etl.fromxml('Cars.xml','row',['Id','Name','Price'])
#table1 = etl.fromxml('Cars.xml','row','Id')

print table1