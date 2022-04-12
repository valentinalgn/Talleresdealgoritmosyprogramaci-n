#Entradas
chelinesaustriacos=float(input("Ingrese la cantidad de chelines austriacos: "))
dracmasgriegos=float(input("Ingrese la cantidad de dracmas griegos: "))
pesetas=float(input("Ingrese la cantidad de pesetas: "))
#Caja negra
pesetas1=chelinesaustriacos*9.56871
pesetas2=dracmasgriegos*0.88607
francofrances=pesetas2/20.110 
dolares=pesetas/122.499
librasitaliana=pesetas/0.09289
#Salida
print("El cambio de Chelines Austriacos a Pesetas es de:",pesetas1)
print("El cambio de Dracmas Griegos a Francos franceses es de:",francofrances)
print("El cambio de Pesetas a Dolares es de:",dolares)
print("El cambio de Pesetas a Libras Italianas es de:",librasitaliana)