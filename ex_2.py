toplam = 0	
n=1
while n< 9000 :
	toplam += (1/n**2)
	n+=1

print("Estimated value of pi is ",(6*toplam)**(1/2))