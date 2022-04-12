#Entradas
nombre=str(input("Ingrese el nombre del trabajador: "))
numerohorastrabajadas=int(input("Ingrese el numero de horas trabajadas: "))
pagoporhora=float(input("Ingrese el valor por hora: "))
numerohorasextras=int(input("Ingrese numero de horas extras: "))
numerohijos=int(input("Ingrese cuantos hijos tiene: "))
#Caja negra
sueldo_base=(numerohorastrabajadas*pagoporhora)
pago_horas=numerohorasextras*(pagoporhora*1.25)
forzosos=(numerohorastrabajadas*pagoporhora)*0.05
politicahabitacional=(numerohorastrabajadas*pagoporhora)*0.02
cajaahorros=(numerohorastrabajadas*pagoporhora)*0.07
extras=(250000+173000*numerohijos+180000)
sueldo_neto=(extras+pago_horas+sueldo_base-forzosos-politicahabitacional-cajaahorros)
asignaciones=pago_horas+extras
deducciones=forzosos+cajaahorros+politicahabitacional
#Salida
print("El trabajador gana un sueldo neto de:",sueldo_neto)
print("El trabajador tiene unas asignaciones de:",asignaciones)
print("El trabajor tiene unas deducciones de:",deducciones)