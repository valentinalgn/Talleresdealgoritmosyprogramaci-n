"""
edad --> int --> E
sexo --> str --> S
nivel de hemoglobina --> float --> n
Salidas
resultados de anemia --> str --> R
"""
# Entradas
from collections import namedtuple
from tkinter.font import names


E=int(input("Ingrese la edad en meses: "))
n=float(input("Digite el nivel de hemoglobina en g%: "))
if(E>180):
    S=str(input("¿Cuál es su sexo? (Hombre:1 o Mujer:2) "))
else:
    S=0
S=int(S)
#Caja negra
if(E>=0 and E<=1):
    if(n>=13 and n<=26):
        R="Negativo"
    elif(n<13):
        R="Positivo"
    else:
        (n>26)
        R="Error"
elif(E>1 and E<=6):
    if(n>=10 and n<=18):
        R="Negativo"
    elif(n<10):
        R="Positivo"
    else:
        (n>18)
        R="Error"
elif(E>6 and E<=12):
    if(n>=11 and n<=15):
        R="Negativo"
    elif(namedtuple<11):
        R="Positivo"
    else:
        (n>15)
        R_="Error"
elif(E>12 and E<=60):
    if(n>=11.5 and n<=15):
        R="Negativo"
    elif(n<11.5):
        R="Positivo"
    else:
        (n>15)
        R="Error"
elif(E>60 and E<=120):
    if(n>=12.6 and n<=15.5):
        R="Negativo"
    elif(n<12.6):
        R="Positivo"
    else:
        (n>15.5)
        R="Error"
elif(E>120 and E<=180):
    if(n>=13 and n<=15.5):
        R="Negativo"
    elif(n<13):
        R="Positivo"
    else:
        (n>15.5)
        R="Error"
elif(E>180 and S==2):
    if(n>=12 and n<=16):
        R="Negativo"
    elif(names<12):
        R="Positivo"
    else:
        (n>16)
        R="Error"
elif(E>180 and S==1):
    if(n>=14 and n<=18):
        R="Negativo"
    elif(n<14):
        R="Positivo"
    else:
        (n>18)
        R="Error"
# Salidas
print(f"Su diagnostico para anemia es: ,R")
