est={}
est.update({
        "1":{
            "nombre":"Lorea",
            "nota": 8
    },
        "2": {
            "nombre":"Markel",
            "nota": 4.2
    }, 
        "3": {
            "nombre":"Julien",
            "nota": 6.5
    }
})
c={}
for i in range (10):
    nombre=input("Nombre estudiante: ")
    nota=int(input("Nota: "))
    c.update({i:{"nombre":nombre,"nota":nota}})

b=[]
a=[]
sum=0
for e in c:
    sum=int(c[e]["nota"])+sum
    if c[e]["nota"]<6:
        b.append(c[e]["nombre"])
    else:
        a.append(c[e]["nombre"])

print("Estudiantes que suspenden:",b)
print("Estudiantes que aprueban:",a)
print("Promedio de la clase:",sum/10)