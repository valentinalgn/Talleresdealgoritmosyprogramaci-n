#Entrada
lecturaanterior=float(input("Ingrese el valor de la lectura anterior: "))
lecturaactual=float(input("Ingrese el valor de la entrada actual: "))
kilovatio=float(input("Ingrese el costo por kilovatio: "))
#Caja negra
lecturatotal=lecturaanterior-lecturaactual
costo=lecturatotal*kilovatio
#Salida
print("El monto que debe pagar por un mes de li electrica es:",costo)
