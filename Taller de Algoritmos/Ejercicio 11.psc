Algoritmo Inicio_descuento
	Escribir 'Escribe las tres calificaciones'
	leer n1,n2,n3
	Escribir 'Escribe la calificacion del examen final'
	leer examen
	Escribir 'Escribe la calificacion del trabajo final'
	leer trabajo
	promedio = (n1+n2+n3)/3
	promedio_final = (promedio*0.55)+(examen*0.30)+(trabajo*0.15)
	Escribir 'El promedio de la materia de algoritmos es: ',promedio_final
FinAlgoritmo
