from common.base.basic import read_file
from common.base.basic import Random

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
		#print array

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
	B = mergesort(A)

	print B

	R = False
	for i in range(len(B) - 1):

		start = i + 1
		end = len(B) - 1
		while start < end:
			mid = (start + end) / 2

			if B[mid] + B[i] == x:
				R = True
				break
			elif B[mid] + B[i] < x:
				start = mid + 1
			elif B[mid] + B[i] > x:
				end = mid - 1

		if B[start] + B[i] == x:		
			R = True

	return R



A = [ Random(0,2) for i in range(100)]
x = 71
#print A
print mergesort(A)
#print problema_3_8(A,x)