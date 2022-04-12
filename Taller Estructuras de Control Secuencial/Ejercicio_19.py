#Entrada
naranjas=int(input("Ingrese el numero de naranjas: "))
valor=float(input("Ingrese el valor por docena de naranjas: "))
venta=float(input("Ingrese el valor que se gano en la venta de todas las naranjas: "))
#Caja negra
ganancia=(venta-naranjas/valor)*100
#Salida
print("El porcentaje de ganancia obtenido es de:",ganancia)
