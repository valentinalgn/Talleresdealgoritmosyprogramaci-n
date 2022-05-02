nombre=[]
porcentaje=[]
f=g=0
while True:
    n=input("Ingrese el nombre del estudio: ")
    p=float(input("Ingrese el puntaje del estudiante: "))
    nombre.append(n)
    porcentaje.append(p)
    c=float(input("¿Desea continuar? Digite 0 para Si y 1 para no "))
    if(c==1):
        break
for k in range ((len(porcentaje))):
    if(porcentaje[k]<(sum(porcentaje)/len(porcentaje))):
        f+=1
    elif(porcentaje[k]>(sum(porcentaje)/len(porcentaje))):
        g+=1
f=round((f*100)/len(porcentaje),2)
g=round((g*100)/len(porcentaje),2)
a=b=0
r=porcentaje[0]
for i in range (len(porcentaje)):
    if(porcentaje[i]>r):
        r=porcentaje[i]
        a=1
print("El estudiante con mayor puntuaje es: ",nombre[a])
for j in range(len(porcentaje)):
    if(porcentaje[j]<r):
        b=j
print("El estudiante con menor puntaje es:",nombre)
print("El puntaje maximo obtenido es: ",max(porcentaje))
print("El puntaje minimo obtenido es:",min(porcentaje))
print("El promedio de todos los puntajes es",round(sum(porcentaje)/len(porcentaje),2))
print("El porcentaje inferior al promedio fue de : ",f)