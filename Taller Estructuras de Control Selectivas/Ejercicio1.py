"""
Entradas
inversion en el banco --> float --> i
tasa de interes --> float --> t
Salidas
dinero total --> float --> d
"""
#Entradas
i=float(input("Ingrese la inversion en el banco: "))
t=float(input("Ingrese la tasa de interes: "))
#Caja negra 
interes=i*t
d=i+interes
if interes>100000:
    print(f"El interes es mayor a 100000 COP: {interes} COP y puede reinvertir")
else:
    print(f"El interes es menor a 100000 COP: {interes} COP ")
print(f"El dinero total en la cuenta es de: ${d} COP")
