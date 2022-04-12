#Entradas
P=float(input("Ingrese el valor de la computadora: "))
T=float(input("Ingrese el valor de cada cuota: "))
#Caja negra
total_cuota=T*12
diferencia=total_cuota-P
porcentaje=(diferencia/P)*100
#Salida
print(f"El porcentaje de recargo si se paga por cuotas es: {porcentaje}%")