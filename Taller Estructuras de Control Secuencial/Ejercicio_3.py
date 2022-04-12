#Entradas
sueldo=float(input("Ingrese el sueldo base: "))
venta1=float(input("Ingrese el valor de la venta 1: "))
venta2=float(input("Ingrese el valor de la venta 2: "))
venta3=float(input("Ingrese el valor de la venta 3: "))
#Caja negra
promedioventas=(venta1+venta2+venta3)/3
sueldototal=sueldo+(promedioventas*0.1)
#Salidas
print("El valor de las comisiones del mes es:",promedioventas)
print("Su sueldo con comisiones incluidas es:",sueldototal)
