#Entrada
pagado=float(input("Ingrese el precio final pagado por el producto: "))
venta=float(input("Ingrese el precio de venta al publico: "))
#Caja negra
diferencia=venta-pagado
descuento=(diferencia/venta)*100
#Salida
print(f"El porcentaje del descuento aplicado al producto es: {descuento} %") 