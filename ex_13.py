for i in range(10,100):
	for j in range(10,100):
		a = int(str(i)[0])
		b = int(str(i)[1])
		c = int(str(j)[0])
		d = int(str(j)[1])
		if a*1000 +b*100 +c*10+d == a*110+c*110+b*11+d*11:
			print("İlk sayı {} ve ikinci sayı {} 'dır".format(i,j))
