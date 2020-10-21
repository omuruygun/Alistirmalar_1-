liste=list()
for i in range(1,350):
	if 125 %i == 200%i == 350%i:
		liste.append(i)
kalan =0
x = None
for a in liste:
	if 125%a > kalan:
		kalan = 125%a
		x= a 
print("En büyük kalanı veren sayı {}'dir".format(x))

