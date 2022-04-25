"""
Entradas
temperatura en grados fahrenheit-->float-->t
Salidas
deporte-->str-->d
"""
#Entradas
t=float("Digite temperatura: ")
#Caja negra
d=""
if(t>85): 
    d="natacion"
elif(t>70 and t<=85): 
    d="tenis"
elif(t>32 and t<=70): 
    d="Golf"
elif(t>10 and t<=32): 
    d="Equi"
elif(t>=0 and t<=10): 
    d="Marcha"
else:
    d="La temperatura no pertenece a ningun deporte"
#Salida
print("El deporte a practicar es: ",d)
