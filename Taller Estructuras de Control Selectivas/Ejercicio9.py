"""
Entradas
Nombre cliente --> str --> N
Compra --> float --> C
Salidas
Nombre cliente --> str --> N
Compra --> float --> C
Total --> float --> T
Descuento --> float --> D
"""
# Entrada 
n=str(input("Escriba su nombre: "))
m=float(input("Digite el valor de su compra: "))
# Caja negra 
if m<50000:
    print("No hay descuento")
if m>500000 and m<=100000:
    d=m*0.05
    print ("Descuento: ",d, "COP")
    print ("Monto a pagar: ", m-d, "COP")
if m>100000 and m<=700000:
    d=m*0.11
    print ("Descuento: ",d, "COP")
    print ("Monto a pagar: ", m-d, "COP")
if m>700000 and m<=1500000:
    d=m*0.18
    print ("Descuento: ",d, "COP")
    print ("Monto a pagar: ", m-d, "COP")
if m>1500000:
    d=m*0.25
    print ("Descuento: ",d, "COP")
    print ("Monto a pagar: ", m-d, "COP") 
