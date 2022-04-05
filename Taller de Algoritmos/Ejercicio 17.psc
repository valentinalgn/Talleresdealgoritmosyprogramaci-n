Algoritmo Inicio_vehiculos
	Escribir 'Escribir la velocidad 1: '
	Leer velocidad1
	Escribir velocidad1 'km/h'
	Escribir 'Escribir la velocidad 2 la cual es mayor a la veloidad 1: '
	Leer velocidad2
	Escribir velocidad2 'km/h'
	Escribir 'Ingrese distancias entre los dos vehiculos'
	Leer distancia
	Escribir distancia 'km'
	tiempo<-((distancia)/(velocidad2-velocidad1))*60
	Escribir 'El tiempo que se tarda' tiempo 'en minutos el vehiculo mas veloz al otro'
FinAlgoritmo
