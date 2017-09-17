def selectionSort(himpunan):
 	for fase in range(len(himpunan)-1,0,-1):
 		print "Fase:",fase
 		posisi_angka_terbesar=0
 		for i in range(1,fase+1):
 			print "     Iterasi ke:",i,"pada fase ke:",fase
 			if himpunan[i]>himpunan[posisi_angka_terbesar]:
 				#print "        Awal:",posisi_angka_terbesar
 				posisi_angka_terbesar_awal= posisi_angka_terbesar
 				posisi_angka_terbesar=i
 				#print "        Akhir:",posisi_angka_terbesar
 				#posisi_angka_terbesar_akhir= posisi_angka_terbesar
 				print "        ",himpunan[i],">",himpunan[posisi_angka_terbesar_awal],"= TRUE. Maka posisi terbesar",i," BERUBAH yaitu:",himpunan[i],". Masuk IF."
 			else:
 				print "        ",himpunan[i],">",himpunan[posisi_angka_terbesar],"= FALSE. Maka posisi terbesar",posisi_angka_terbesar,"TETAP yaitu:",himpunan[posisi_angka_terbesar],". Masuk ELSE."
 			
 		print "Angka yang di swap yaitu urutan akhir ke:",i,"yaitu",himpunan[i],":",himpunan[posisi_angka_terbesar]
 		himpunan[i],himpunan[posisi_angka_terbesar] = himpunan[posisi_angka_terbesar],himpunan[i]
 		print "Di swap menjadi:",himpunan[i],":",himpunan[posisi_angka_terbesar]
himpunan = [40,35,82,80,8,13,59]
print 'Data Awal:',himpunan
selectionSort(himpunan)
print 'Data Urut:',himpunan