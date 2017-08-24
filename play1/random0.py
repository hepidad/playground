import random,timeit

himpunan=[]

for i in range(0,100):
	himpunan.append(random.randint(1,99))

start_time = timeit.default_timer()

if 19 in himpunan:
	hasil =  "True"

waktu = (timeit.default_timer() - start_time)

print himpunan
print "Output:",hasil
print "Time:", format(waktu,'.10f')
