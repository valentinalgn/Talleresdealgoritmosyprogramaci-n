a=int(input("Digite el primer número (Dividendo): "))
b=int(input("Digite el Segundo número (Cociente): "))
c=0
while a>0:
    a=a-b
    c=c+1
print("El resto de la division es: ",a)
print("El valor del cociente es: ",c)