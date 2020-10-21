liste= list()
for i in range(2,int(121212/2)+1):
	if 121212%i == 0 :
		liste.append(i)

fark =None 
sayı1=None 
sayı2=None
for a in liste :
	if fark == None :
		fark= abs(a-(121212/a))

	elif abs(a-(121212/a)) < fark :
		fark= abs(a-(121212/a))
		sayı1= a
		sayı2=int(121212/a)

print("Birinci sayı = {} \nİkinci Sayı {} ".format(sayı1,sayı2))

