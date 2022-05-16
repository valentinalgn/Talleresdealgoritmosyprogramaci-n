archivo = open('paises.txt', 'r')
#imprima la posicion de colombia
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Colombia: Bogotá\n"):
    break
  lista=[]   
print(c)
"""
#Imprima todos los paises
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
"""
#Imprima todas las Capitales
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
"""  
#Imprimir todos los paises que inicien con la letra C
"""
lista=[]
paises=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
for i in paises:
  if(i[0]=="C"):
    print(i)
"""  
#imprima todas las capitales que inicien con la leta B
"""
lista=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
  if(i[0]=="B"):
    print(i)  
"""
#Cuente e imprima cuantas ciudades inician con la latra M  
"""
lista=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
  if(i[0]=="M"):
    print(i) 
"""
#Imprima todos los paises y capitales, cuyo inicio sea con la letra U
"""
lista=[]
lista2=[]
ciudades=[]
paisu=[]
for i in archivo:
  e=i.index(":")
  for q in range(e+2, len(i)-1):
    lista.append(i[q])
    e="".join(lista)
  ciudades.append(e)
  lista=[]
  n=i.index(":")
  for t in range(0, n):
    lista2.append(i[t])
    n="".join(lista2)
  paisu.append(n)
  lista2=[]
print("Las ciudades cuya inical es u, son:\n")
for i in ciudad:
  if(i[0]=="U"):
    print(i)
print("Los paises cuya inicial es u, son:\n")
for i in pais:
  if(i[0]=="U"):
    print(i,"\n")  
"""
#Cuente e imprima cuantos paises que hay en el archivo
"""
c=0
lista=[]
for i in archivo:
  a=i.index(":")
  c=c+1
  for j in range(0,a):
    lista.append(i[j])
  a="".join(lista)
  lista=[]
  print(c,a)
"""
#Busque e imprima la ciudad de Singapur
"""
lista=[]
for i in archivo:
  lista.append(i)
  x="".join(lista)
  if(x[0]=="S" and x[1]=="i" and x[2]=="n" and x[3]=="g" and x[4]=="a" and x[5]=="p" and x[6]=="u" and x[7]=="r"):
    y=x.index(":")
    lista=[]
    break
  lista=[]
for i in range(y+2,len(x)):
  lista.append(x[i])
x="".join(lista)
print(x)
"""
#Busque e imprima el pais de Venezuela y su capital
"""
lista=[]
for j in archivo:
  lista.append(j)
  x="".join(lista)
  if(x[0]=="V" and x[1]=="e" and x[2]=="n" and x[3]=="e" and x[4]=="z" and x[5]=="u" and x[6]=="e" and x[7]=="l" and x[8]=="a"):
    break
  lista=[]
print(x)
"""
#Cuente e imprima las ciudades que su pais inicie con la letra E
"""
c=0
lista=[]
pais=[]
for i in archivo:
  a=len(i)
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  pais.append(a)
  lista=[]
for j in pais:
  if(j[0]=="E"):
    a=j.index(":")
    c=c+1
    for r in range(a+2,len(j)):
      lista.append(j[r])
    a="".join(lista)
    lista=[]
    print(c,a)
"""
#Buesque e imprima la Capiltal de Colombia
"""
lista=[]
for i in archivo:
  lista.append(i)
  x="".join(lista)
  if(x[0]=="C" and x[1]=="o" and x[2]=="l" and x[3]=="o" and x[4]=="m" and x[5]=="b" and x[6]=="i" and x[7]=="a"):
    y=x.index(":")
    lista=[]
    break
  lista=[]
for i in range(y+2,len(x)):
  lista.append(x[i])
x="".join(lista)
print(x)
"""
#imprima la posicion del pais de Uganda
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a="".join(lista)
  c=c+1 
  if(a=="Uganda: Kampala\n"):
    break
  lista=[]   
print(c)
"""
#imprima la posicion del pais de Mexico
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a="".join(lista)
  c=c+1 
  if(a=="México: Ciudad de México \n"):
    break
  lista=[]   
print(c)
"""
#El alcalde de Antananarivo contrato a algunos alumnos de la Universidad Ean para corregir el archivo de países.txt, ya que la capital de Madagascar NO es rey julien es Antananarivo, espero que el alcalde se vaya contento por su trabajo. Utilice un For para cambiar ese Dato
"""
lista=[]
for i in archivo:
    lista.append(i)
archivo1=open("paises.txt","w")
for i in lista:
    if(i=="Madagascar: rey julien\n"):
      archivo1.write("Madagascar: Antananarivo\n")
    else:
        archivo1.write(i)
archivo1.close()
"""
#Agregue un país que no esté en la lista 
"""
pais = "Daguestán: Majachkalá"
archivo2 = open("paises.txt", "a")
archivo2.write("\n" + pais + "\n")
archivo2.close()
"""
archivo.close()