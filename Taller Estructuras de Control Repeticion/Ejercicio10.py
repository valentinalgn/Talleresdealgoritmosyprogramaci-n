c=int(input("Ingrese la cantidad de estudiantes: "))
a=0
for i in range(1,c+1):
    altura=float(input("Ingrese  la altura: "))
    if(a<=altura):
        a=altura
    
print(a)