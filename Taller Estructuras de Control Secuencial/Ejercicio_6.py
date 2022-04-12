#Entradas
mujeres=int(input("Digite la cantidad de mujeres que hay: "))
hombres=int(input("Digite la cantidad de hombres que hay: "))
#Caja negra
Totalestudiantes=mujeres+hombres#int
mujeresp=(mujeres*100)/Totalestudiantes#float
hombresp=(hombres*100)/Totalestudiantes#float
#Salidas
print(f"El porcentaje de mujeres es: {round(mujeresp,2)} y el porcentaje de hombres es: {round(hombresp,2)}")#str5