# Lab-01. Busqueda lineal y binaria. Ordenamiento por insercion. Experimentos. Analisis de resultados.

# Integrantes:
# <colocar nombre, apellido y carnet de cada integrante del grupo>

# extender el limite de la profundidad del stack de recursion
from sys import setrecursionlimit
from sys import path
setrecursionlimit(int(1e6))
path.insert(0, '..')

# importar base
from common.base.basic import read_file
from common.base.basic import Random
from common.base.test_lab_01 import test_sort
from common.base.test_lab_02 import test_freivalds
from common.base.test_lab_02 import test_amplified_freivalds
from common.base.test_lab_02 import test_problema_3_8

from common.base.sort import native_sort
from common.base.sort import verifier_sort
from common.base.problema_3_8 import verifier_problema_3_8


########################################################################

def mergesort(A):

	# Busca la cantidad de elementos del arreglo.
	r = len(A)

	# Si el arreglo es unitario esta ordenado por definicion.
	if 1 == r: return A

	# Crea dos nuevos sub-arreglos ordenados.
	# L para el sub-arreglo de la izquierda (Left).
	# R para el sub-arreglo de la derecha (Right).
	L = mergesort(A[:(r/2)])
	R = mergesort(A[(r/2):])
	
	# Delvuelve el arreglo ordenado.
	return merge(L,R)

	
def merge(L,R):

	# Crea un nuevo arreglo vacio donde se guardaran los valores ordenados.
	array = []

	# Inicializa las variable para iterar sobre los sub-arreglos.
	i,j = 0,0

	# Inicializa las variables para ver si los arreglos ya han sido recorridos.
	a,b = len(L),len(R)

	# Mientras el valor del iterador este en el rango del sub arreglo, entra en el condicional.
	while (i < a or j < b):

		# El condicional fue implementado de esta manera ya que las guardias en python son
		# deterministas. De esta forma la tercera y la cuarta guardia no dan error ya que
		# entra en la primera o segunda guardia si el indice a comparar esta fuera del rango
		# del arreglo.

		if (i >= a): # Chequea si ya recorrio el arreglo L completo.
			array.append(R[j])
			j += 1
		elif (j >= b): # Chequea si ya recorrio el arreglo R completo.
			array.append(L[i])
			i += 1
		elif (L[i] <= R[j]): # Asigna el menor de los elementos.
			array.append(L[i])
			i += 1
		elif (R[j] < L[i]): # Asigna el menor de los elementos.
			array.append(R[j])
			j += 1

	return array

def insertion_sort(A):
	for i in range(1, len(A)):
		key = A[i]

		j = i - 1
		while j >= 0 and A[j] > key:
			A[j+1] = A[j]
			j = j - 1
		A[j+1] = key

def freivalds(n, A, B, C):

	def multiply(n, A, Z):
		# Crea el vector a retornar
		R = n * [0]

		# Recorre los elementos del vector R y las filas de la matriz A 
		for i in range(n):
			# Recorre los elementos del vector Z y los elementos de la fila i de A
			for j in range(n):
				R[i] = R[i] + (A[i][j] * Z[j])
		return R
	# Genera un vector Z lleno de ceros y unos
	Z = n * [n]
	for i in range(n):
		Z[i] = Random(0,1)
	# Multiplica B x Z, luego A x (B x Z) y C x Z
	# Obteniendo 2 vectores x1 y x2 de largo n
	Y = multiply(n, B, Z)
	x1 = multiply(n, A, Y)
	x2 = multiply(n, C, Z)

	# Chequea si A x (B x Z) = C x Z
	return x1 == x2

def amplified_freivalds(k, n, A, B, C):
    for i in range(k):
        r = freivalds(n, A, B, C)
        if r == False:
            return False
    return True


def problema_3_8(A, x):
	# Se crea un arreglo B con los elementos de A ordenado usando mergesort sobre A
	B = mergesort(A)

	# Variable que sera devuelta, se inicia en False en y se asigna True en caso de conseguir una ocurrencia
	R = False

	# Ciclo que va recorriendo todos los elementos de B y busca en el resto con busqueda
	# binaria algun elemento que sumado con el i-esimo resulte x 
	for i in range(len(B) - 1):

		# Inicializa start en el elemento siguiente al que se quiere comparar
		start = i + 1
		end = len(B) - 1

		# Verifica que el arreglo tenga mas de un elemento
		while start < end:

			# Elemento medio del arreglo usado para la busqueda binaria
			mid = (start + end) / 2

			if B[mid] + B[i] == x:
				# Si el elemento medio del arreglo mas el elemento en la i-esima posicion es igual a x, asigna R = True y sale del ciclo
				R = True
				break

			elif B[mid] + B[i] < x:
				# Si la suma del elemento medio con el i-esimo es menor que x, descarta mitad izquierda del arreglo
				start = mid + 1

			elif B[mid] + B[i] > x:
				# Si la suma del elemento medio con el i-esimo es mayor que x, descarta la mitad derecha del arreglo
				end = mid - 1

		if B[start] + B[i] == x:		
			# Al finalizar el ciclo, si no se ha conseguido el elemento buscado, quedara un arreglo de un solo elemento, si este elemento sumado con el i-esimo resulta
			# x, se asigna R = True
			R = True

	return R


########################################################################


# leer los datos y preparar variables para correr experimentos
data = read_file('data/web2')
sizes = [ 2**i for i in range(16) ]
fractions = [ .5, .05, .005, .0005]
runs_for_each_size = 50
runs_for_each_size_and_fraction = 3
amplification = 20

# imprimir encabezado de resultados
print 'type,name,size,i,time,verification'

# experimentos para algoritmos de ordenamiento
test_sort('nativo', sizes, fractions, data, runs_for_each_size_and_fraction, native_sort, verifier_sort)
test_sort('insertion', sizes[:-1], fractions, data, runs_for_each_size_and_fraction, insertion_sort, verifier_sort)
test_sort('mergesort', sizes, fractions, data, runs_for_each_size_and_fraction, mergesort, verifier_sort)

# experimentos para freivalds
test_freivalds("freivalds", [ 2, 4, 8, 16, 32, 64, 128 ], 0, 30, runs_for_each_size, freivalds)
test_amplified_freivalds("amplified-freivalds", [ 2, 4, 8, 16, 32, 64, 128 ], 0, 30, runs_for_each_size, amplified_freivalds, 50)

# preparar datos para problema 3.8
test_problema_3_8("problema-3-8", [ 2**i for i in [ 4, 6, 8, 10, 12, 14, 16 ] ], 100, 10000, runs_for_each_size, problema_3_8, verifier_problema_3_8)

