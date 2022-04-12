#Entrada
n1=int(input("Ingrese la cantidad de billetes 50000: "))
n2=int(input("Ingrese la cantidad de billetes 20000: "))
n3=int(input("Ingrese la cantidad de billetes 10000: "))
n4=int(input("Ingrese la cantidad de billetes 5000: "))
n5=int(input("Ingrese la cantidad de billetes 2000: "))
n6=int(input("Ingrese la cantidad de billetes 1000: "))
n7=int(input("Ingrese la cantidad de billetes 500: "))
n8=int(input("Ingrese la cantidad de billetes 100: "))
#Caja negra
N1=n1*50000
N2=n2*20000
N3=n3*10000
N4=n3*5000
N5=n5*2000
N6=n6*1000
N7=n7*500
N8=n8*100
total=N1+N2+N3+N4+N5+N6+N7+N8
#Salida
print("El total de dinero que hay en el banco es:",total)