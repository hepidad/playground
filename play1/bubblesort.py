def bubbleSort(himpunan):
	n=len(himpunan)
	for fase in range(n-1,0,-1):
		for i in range(fase):
			if himpunan[i]>himpunan[i+1]:
				himpunan[i],himpunan[i+1] = himpunan[i+1],himpunan[i]

himpunan = [40,35,82,80,8,13,59]
print 'Data Awal:',himpunan
bubbleSort(himpunan)
print 'Data Urut:',himpunan