def asal_mı(x):
        if x== 0 or x == 1 :
                return False
        else:
                
                sayac=0
                for i in range(2,x):
                        if x%i == 0:
                                sayac+=1
                                break 
                if sayac== 0:
                        return True 
                else:
                        return False

liste=list()
for i in range(1000,10000):
	if asal_mı(i) == True :
		liste.append(i)
print(liste)
