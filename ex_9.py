
for i in range(1,1000):
	if i<10:
		if i!=9:
			print(i,end=" ")
	elif i<100:
		if int(str(i)[0]) +int(str(i)[1])	<9:
			print(i,end=" ")
	else:
		if int(str(i)[0]) +int(str(i)[1]) + int(str(i)[2]) < 9 :
			print(i,end=" ")


