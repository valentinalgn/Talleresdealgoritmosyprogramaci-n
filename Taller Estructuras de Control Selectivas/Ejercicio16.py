"""
Entradas
A --> float --> a
B --> float --> b
C --> float --> c
Caja negra
discriminante --> d
Salidas
X1 --> float --> x1
X2 --> float --> x2
"""
#Entradas
a=float(input(" A: "))
b=float(input(" B: "))
c=float(input(" C: "))
#Caja negra
d=b**2-(4*a*c)
x1=0.0#variable global
x2=0.0
if d==0:
    x1=x2=-b/(2*a)
elif d>0:
    x1=(-b+(b**2-4*a*c)**(0.5))/(2*a)
    x2=(-b-(b**2-4*a*c)**(0.5))/(2*a)
else:
    x1=x2="No tiene solucion en bases reales"
#Salidas
print(f"El valor de X1 es: {x1}")
print(f"El valor de X2 es: {x2}")
