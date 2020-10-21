import math
toplam = 0
i = 0
while i<25 :
	toplam += 1/math.factorial(i)
	i +=1
print("Estimated Value of e is " , toplam)
