import random, timeit

himpunan=[]

himpunan = random.sample(xrange(0,100000001),100000) 

start_time = timeit.default_timer()

if 21145282 in himpunan:
	hasil = "True"
else:
	hasil =  "False"

waktu = (timeit.default_timer() - start_time)

print himpunan
print "Output:",hasil
print "Time:", format(waktu,'.10f'),'sec.'