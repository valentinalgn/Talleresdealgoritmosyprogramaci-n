"""
Entradas
sueldo bruto --> float --> b
Salidas
sueldo neto --> float ..> n
"""
#Entradas
b=float(input("Ingrese el salario: "))
#Caja negra
if(b<900000):
    n=(b*0.15)+b
else:
    n=(b*0.12)+b
print("El salario con aumento es: ",n)