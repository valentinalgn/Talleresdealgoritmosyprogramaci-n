
s=float(input("Ingrese el salario: "))
d1=float(input("Ingrese importe global de las ventas del departamento 1: "))
d2=float(input("Ingrese importe global de las ventas del departamento 2: "))
d3=float(input("Ingrese importe global de las ventas del departamento 3: "))
v=d1+d2+d3
p=v*0.33
if(d1>p):
    print("Los vendedores del departamento 1 recibiran:",(s*0.20)+s,"COP")
else:
    print("Los vendedores del departamento 1 recibiran:",s,"COP")
if(d2>p):
    print("Los vendedores del departamento 2 recibiran:",(s*0.20)+s,"COP")
else:
    print("Los vendedores del departamento 2 recibiran:",s,"COP")
if(d3>p):
    print("Los vendedores del departamento 3 recibiran:",(s*0.20)+s,"COP")
else:
    print("Los vendedores del departamento 3 recibiran:",s,"COP")
    