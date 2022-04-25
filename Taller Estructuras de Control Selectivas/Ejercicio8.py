"""
Entradas
datos --> int --> p,q
Salidas
expresion --> str --> e
"""
#Entradas
p=int(input("Ingrese el valor de P: "))
q=int(input("Ingrese el valor de Q: "))
#Caja negra
e=(p**3)+(q**4)-(2*(p**2))
if (e>680):
    print("Los valores","P=",p,"y Q=",q,"satisfacen los valores",e,">680")
else:
    print("Los valores","P=",p,"y Q=",q,"no satisfacen los valores",e,"<680")
