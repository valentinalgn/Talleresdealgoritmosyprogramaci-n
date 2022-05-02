suma=0
c=0
for k in range(1,1000):
    suma=round(suma+((k**2)+1)/k)
    if(suma<=1000):
        c=c+1
print (c)