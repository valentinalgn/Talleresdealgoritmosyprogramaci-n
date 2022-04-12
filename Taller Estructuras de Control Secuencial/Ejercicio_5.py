#Entrada
nota1=float(input("Ingrese la nota 1: "))
nota2=float(input("Ingrese la nota 2: "))
nota3=float(input("Ingrese la nota 3: "))
examen=float(input("Ingrese la nota del examen: "))
trabajofinal=float(input("Ingrese la nota del trabajo final: "))
#Caja negra
promedio_notasparciales=(nota1+nota2+nota3)/3
promedio=promedio_notasparciales*0.55
notaexamen=examen*0.30
notatrabajofinal=trabajofinal*0.15
notafinal=promedio+notaexamen+notatrabajofinal
#Salidas
print("Su nota final de la materia es:",notafinal)