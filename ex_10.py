sayac = 0
liste=list()
for i in range(10000,100000):
	if str(i)[0:2]== str(i)[3:5]:
		liste.append(i)
		sayac+=1
print(liste)
print(sayac)

