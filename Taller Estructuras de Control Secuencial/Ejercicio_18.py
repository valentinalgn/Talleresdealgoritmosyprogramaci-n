#Cntradas
capital=float(input("Ingrese la cantidad el prestamo realizado: "))
pagado=float(input("Ingrese la cantidad del prestamo pagada:"))
tiempo=int(input("Ingrese el tiempo del prestamo en años:"))
#Caja negra
interes=(pagado-capital)/capital
razon=(interes*100)/(capital*tiempo)
porcentajeinteres=(capital*tiempo*razon)/100
#Salida
print("El porcentaje ha pagar de interes en un año es:",porcentajeinteres)