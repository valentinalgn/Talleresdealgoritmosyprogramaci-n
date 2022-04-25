"""
Entradas
datos-->int-->a,b,c,d
Salidas
resultado-->float--> n
"""
#Entradas
d=input("Ingrese los datos a,b,c,d: ").split(",")
a,b,c,d=d.split(",")
a=int(a)
b=int(b)
c=int(c)
d=int(d)
#Caja negra
if(d==0):
    n=(a-c)**2
elif(d>0):
    n=((a-b)**3)/d
    print("El resultado es: ",n)
