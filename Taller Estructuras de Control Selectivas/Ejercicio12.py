"""
Entradas
Monto en COP --> float --> M
Salidas
Billetes de 100000 --> int --> x
Billetes de 50000 --> int --> b
Billetes de 20000 --> int --> c
Billetes de 10000 --> int --> e
Billetes de 5000 --> int --> f
Billetes de 2000 --> int --> g
Billetes de 1000 --> int --> h
Monedas de 500 --> int --> i
Monedas de 200 --> int --> j
Monedas de 100 --> int --> k
Monedas de 50 --> int --> l
"""
# Entradas
d=int(input("Cantidad de dinero(COP): "))
#Caja negra
a=int(d/100000)
x=d%100000
b=int(x/50000)
c=int((x%50000)/20000)
e=int(((x%50000)%20000)/10000)
f=int((((x%50000)%20000)%10000)/5000)
g=int(((((x%50000)%20000)%10000)%5000)/2000)
h=int((((((x%50000)%20000)%10000)%5000)%2000)/1000)
i=int(((((((x%50000)%20000)%10000)%5000)%2000)%1000)/500)
j=int((((((((x%50000)%20000)%10000)%5000)%2000)%1000)%500)/200)
k=int(((((((((x%50000)%20000)%10000)%5000)%2000)%1000)%500)%200)/100)
l=int((((((((((x%50000)%20000)%10000)%5000)%2000)%1000)%500)%200)%100)/50)
#Salidas
if a>=1:
    print(a,"Billetes de 100.000")
if b>=1:
    print(b,"Billetes de 50.000")
if c>=1:
    print(c,"Billetes de 20.000")
if e>=1:
    print(e,"Billetes de 10.000")
if f>=1:
    print(f,"Billetes de 5.000")
if g>=1:
    print(g,"Billetes de 2.000")
if h>=1:
    print(h,"Billetes de 1.000")
if i>=1:
    print(i,"Monedas de 500")
if j>=1:
    print(j,"Monedas de 200")
if k>=1:
    print(k,"Monedas de 100")
if l>=1: 
    print(l,"Monedas de 50")