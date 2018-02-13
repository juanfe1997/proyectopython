
def OrdenarDato(ListaDatos):

	Cantidadnumeros = len(ListaDatos)

	for i in range(Cantidadnumeros):
		for a in range(Cantidadnumeros - 1):
			if ListaDatos[a] > ListaDatos[a+1]:
				tmp = ListaDatos[a + 1]
				ListaDatos[a + 1] = ListaDatos [a]
				ListaDatos[a] = tmp

def Mediana(listaDatos):
	
	Cantidadnumeros = len(listaDatos)

	if Cantidadnumeros % 2 == 0:
		medio_1 = int(Cantidadnumeros/ 2) - 1
		medio_2 = (int(Cantidadnumeros / 2))

		medio = (listaDatos[medio_1] + listaDatos[medio_2]) / 2
		print("la mediana es: " + str(medio))

	else:
		medio = (int(Cantidadnumeros / 2)) + 1
		print("la mediana es: " + str(medio))

def Moda(ListaDatos):

	maximo = 0
	posicion = 0

	for i in range(len(ListaDatos)):
		tmp = ListaDatos[i]
		contador = 0
		for a in range(len(ListaDatos)):
			if tmp == ListaDatos[a]:
				contador += 1
		if maximo < contador:
			posicion = i
			maximo = contador

	print("la moda es: " + str(ListaDatos[posicion]))

def Media(ListaDatos):
	suma = 0
	for i in ListaDatos:
		suma += i
	promedio = suma / len(ListaDatos)
	return promedio

def MediaM(ListaDatos):
	promedio = Media(ListaDatos)
	print("El promedio es: "+ str(promedio))

def Varianza(ListaDatos):

	promedio = Media(ListaDatos)
	NumeroDatos = len(ListaDatos)
	acumulador = 0

	for i in ListaDatos:
		formula = ((i - promedio) ** 2) / (NumeroDatos - 1)
		acumulador += formula

	print("la varianza es: " + str(acumulador))

if __name__ == '__main__':

	listaDatos=[]

	NumeroDatos = (int) (input("ingresar el numero de datos de la lista: "))

	for i in range (NumeroDatos):
		Dato = input("ingresar datos: ")
		listaDatos.append(int(Dato))
		print(listaDatos)

	OrdenarDato(listaDatos)
	print(listaDatos)
	Mediana(listaDatos)
	Moda(listaDatos)
	MediaM(listaDatos)
	Varianza(listaDatos)
