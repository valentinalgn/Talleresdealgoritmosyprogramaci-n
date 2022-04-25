"""
Entradas
monto total de la compra --> float --> t
Salidas
fondo de la empresa --> float --> f
cantidad credito --> float --> c
intereses --> float --> i
prestamo banco --> float --> p
"""
# Entradas 
t=float(input("Ingrese el valor total de la compra "))
# Caja negra 
if (t>5000000):
    f=float(t*0.55)
    c=float(t*0.25)
    p=float(t*0.30)
    i=float(c*0.20)
else:
    f=float(t*0.70)
    c=float(t*0.30)
    i=float(c*0.20)
    p=0
# Salida 
print(f"Los fondos utilizados de la empresa son: {f}")
print(f"El credito al fabricante es de: {c}")
print(f"Por intereses del fabricante se tiene: {i}")
print(f"El prestamo del banco es de: {p}")
