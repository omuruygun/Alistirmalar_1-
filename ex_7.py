liste= list()
sayac = 0 
for i in range(100,1000):
	if (int(str(i)[0]) +int(str(i)[1])) == int(str(i)[2]):
		liste.append(i)
		sayac+=1
print("{} adet  3 basamaklı sayının ilk iki rakamının toplamı üçüncü rakama eşittir. ".format(sayac))
print("Bu sayılar şunlardır:",liste)