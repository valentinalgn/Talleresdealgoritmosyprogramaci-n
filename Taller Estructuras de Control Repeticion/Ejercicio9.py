n=0
a=0
b=0
c=0
print("Ingrese 1 para Alcohol, 2 para Gasolina, 3 para Diesel y 4 para finalizar")
while n!=4:
    n=int(input())
    if n>4:
        print("El número debe ser menor que 4")
    else:
        if n==1:
            a=a+1
        elif n==2:
            b=b+1
        elif n==3:
            c=c+1
        else:
            break
print("MUITO OBRIGADO")
print("Alcohol: ", a)
print("Gasolina: ", b)
print("Diesel: ", c)