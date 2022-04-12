import math
#Entrada
a=float(input("Ingrese el lado a:"))
b=float(input("Ingrese el lado b:"))
c=float(input("Ingrese el lado c:"))
#Caja negra
semip=(a+b+c)/2
area=math.sqrt(semip*(semip-a)*(semip-b)*(semip-c))
#Salida
print("El área del triangulo es:",round(area,2))