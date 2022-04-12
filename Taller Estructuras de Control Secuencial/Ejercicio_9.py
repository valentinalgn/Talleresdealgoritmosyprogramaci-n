#Entrada
horas=int(input("Ingrese el número de horas: "))
preciohora=float(input("Ingrese el precio por hora:"))
sueldobase=float(input("Ingrese el sueldo base: "))
#Caja negra
descuento=sueldobase*0.20
salarioneto=horas*preciohora-descuento
#Salida
print("E salario neto del trabajador es:",salarioneto)