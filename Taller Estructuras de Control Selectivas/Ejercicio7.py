"""
Entradas
distancia recorrida --> float --> d
Salidas
monto a pagar --> float --> m
"""
# Entradas
d=float(input("Ingrese los kilometros recorridos: "))
# Caja Negra
if(d<=300):
    m=50000
elif(d>300 and d<1000):
    m=70000+(d-300)*30000
else:
    m=150000+(d-1000)*9000
# Salidas
print(f"El monto a pagar es de: ",m)