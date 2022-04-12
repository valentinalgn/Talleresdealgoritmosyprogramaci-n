#Entradas
#Matematicas
examenmatematicas=float(input("Ingrese la nota del examen de matematicas: "))
tarea1m=float(input("Ingrese la nota de la tarea 1: "))
tarea2m=float(input("Ingrese la nota de la tarea 2: "))
tarea3m=float(input("Ingrese la nota de la tarea 3: "))
#Fisica
examenfisica=float(input("Ingrese la nota del examen de fisica: "))
tarea1f=float(input("Ingrese la nota de la tarea 1: "))
tarea2f=float(input("Ingrese la nota de la tarea 2: "))
#Quimica
examenquimica=float(input("Ingrese la noat del examen de quimica: "))
tarea1q=float(input("Ingrese la nota de la tarea 1: "))
tarea2q=float(input("Ingrese la nota de la tarea 2: "))
tarea3q=float(input("Ingrese la nota de la tarea 3: "))
#Caja negra
promediomatematicas=examenmatematicas*0.9+((tarea1m+tarea2m+tarea3m)/3)*0.10
promediofisica=examenfisica*0.8+((tarea1f+tarea2f)/2)*0.20
promedioquimica=examenquimica*0.85+((tarea1q+tarea2q+tarea3q)/3)*0.15
promediogeneral=(promediomatematicas+promediofisica+promedioquimica)/3
#Salidas
print(f"El promedio general del estudiante es: {promediogeneral}")