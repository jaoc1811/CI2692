# Lab-04. Ordenamiento por claves

# Integrantes:
# Juan Oropeza 15-11041

# importar base
from common.base.basic import read_file
from common.base.basic import Random
from common.base.test_lab_04 import test_sort_by_key

from common.base.sort import verifier_sort


########################################################################


def mergesort(values, sortBy):

	# Busca la cantidad de elementos del arreglo.
	r = len(sortBy)
	# Si el arreglo es unitario esta ordenado por definicion.
	if 1 == r: return values, sortBy

	# Crea dos nuevos sub-arreglos ordenados.
	# L para el sub-arreglo de la izquierda (Left).
	# R para el sub-arreglo de la derecha (Right).
	Lvalues, LsortBy = mergesort(values[:(r/2)], sortBy[:(r/2)])
	Rvalues, RsortBy = mergesort(values[(r/2):], sortBy[(r/2):])
	

	# Delvuelve el arreglo ordenado.
	return merge(Lvalues,Rvalues,LsortBy,RsortBy)

	
def merge(Lvalues,Rvalues,LsortBy,RsortBy):

	# Crea un nuevo arreglo vacio donde se guardaran los valores ordenados.
	values = []
	sortBy = []

	# Inicializa las variable para iterar sobre los sub-arreglos.
	i,j = 0,0

	# Inicializa las variables para ver si los arreglos ya han sido recorridos.
	a,b = len(LsortBy),len(RsortBy)

	# Mientras el valor del iterador este en el rango del sub arreglo, entra en el condicional.
	while (i < a or j < b):

		# El condicional fue implementado de esta manera ya que las guardias en python son
		# deterministas. De esta forma la tercera y la cuarta guardia no dan error ya que
		# entra en la primera o segunda guardia si el indice a comparar esta fuera del rango
		# del arreglo.

		if (i >= a): # Chequea si ya recorrio el arreglo L completo.
			sortBy.append(RsortBy[j])
			values.append(Rvalues[j])
			j += 1
		elif (j >= b): # Chequea si ya recorrio el arreglo R completo.
			sortBy.append(LsortBy[i])
			values.append(Lvalues[i])
			i += 1
		elif (LsortBy[i] <= RsortBy[j]): # Asigna el menor de los elementos.
			sortBy.append(LsortBy[i])
			values.append(Lvalues[i])
			i += 1
		elif (RsortBy[j] < LsortBy[i]): # Asigna el menor de los elementos.
			sortBy.append(RsortBy[j])
			values.append(Rvalues[j])
			j += 1

	return values, sortBy

#### QUICKSORT

# aplica quicksort al arreglo A
def quicksort(values, sortBy):
    quicksort_rec(values, sortBy, 0, len(sortBy) - 1, partition)

# aplica quicksort randomizado al arreglo A
def quicksort_randomized(values, sortBy):
    quicksort_rec(values, sortBy, 0, len(sortBy) - 1, partition_randomized)

# funcion de particion para quicksort deterministico sobre el arreglo A[p...r]
def partition(values,sortBy, p, r):
    pivot = sortBy[r]
    return partition_with_pivot(values, sortBy, p, r, pivot)

# funcion de particion para quicksort randomizado sobre el arreglo A[p...r]
def partition_randomized(values,sortBy, p, r):
    pivot_index = Random(p, r)
    pivot1 = sortBy[pivot_index]
    pivot2 = values[pivot_index]
    sortBy[pivot_index] = sortBy[r]
    values[pivot_index] = values[r]
    values[r] = pivot2
    sortBy[r] = pivot1
    return partition_with_pivot(values, sortBy, p, r, pivot1)

# aplica quicksort con funcion de particion dada al arreglo A[p...r]
def quicksort_rec(values, sortBy, p, r, partition_function):
    if p < r:
        l, m = partition_function(values ,sortBy,p,r)
        quicksort_rec(values, sortBy, p, l - 1, partition_function)
        quicksort_rec(values, sortBy, m + 1, r, partition_function)

# funcion de particion con pivote dado. El ultimo elemento en el
# arreglo es igual al pivote. La funcion retorna dos indices l,m
# tales que:
#   *  A[i] < pivot para p <= i < l
#   *  A[i] == pivot para l <= i <= m
#   *  A[i] > pivot para m < i <= r
#
# La funcion es simiular a la vista en clase excepto que para el lazo
# principal hay tres indices i, j, k tales que el siguiente invariante
# se mantiene:
#   * elementos A[p], A[p+1], ..., A[i] son < pivot
#   * elementos A[i+1], A[i+2], ..., A[j-1] son > pivot
#   * elementos A[j], A[j+1], ..., A[k-1] son "desconocidos"
#   * elementos A[k], A[k+1], ..., A[r] son == pivot
#
# Inicialmente, i = p-1, j = p, y k = r. El procedimiento tiene un 
# lazo principlan y corre en tiempo linear.
#
# Una vez que el lazo principal termina, se deben mover los elementos
# A[k], A[k+1], ..., A[r] que son iguales al pivote al "medio" del 
# arreglo en las posiciones A[l], A[l+1], ..., A[m]
def partition_with_pivot(values, sortBy, p, r, pivot):

    i = p - 1
    k = r
    j = p

    while j < k:
        if sortBy[j] < pivot:
            i = i + 1
            sortBy[i], sortBy[j] = sortBy[j] , sortBy[i]
            values[i], values[j] = values[j] , values[i]
            j = j + 1
        elif sortBy[j] == pivot:
            k = k - 1
            sortBy[j] , sortBy[k] = sortBy[k],sortBy[j]
            values[j] , values[k] = values[k],values[j]
        else:
            j = j + 1


    for q in range(r - k + 1):
        sortBy[k + q], sortBy[i + 1 + q] = sortBy[i + 1 + q], sortBy[k + q]
        values[k + q], values[i + 1 + q] = values[i + 1 + q], values[k + q]

    return i + 1, i + r - k + 1

# Para retornar los indices l,m en la funcion partition_with_pivot, 
# utilice 'return l, m'

# Para recibir los indices l,m en la llama da partition_function en la
# funcion quicksort_rec, utilice 'l, m = partition_function(A, p, r)'



#######################################################################


# leer los datos y preparar variables para correr experimentos
(values,keys) = read_file('data/cursos.txt')
sizes = [ 2**i for i in range(14) ]
fractions = [ .5, .05, .005, .0005]
runs_for_each_size = 50
runs_for_each_size_and_fraction = 3
amplification = 20

# imprimir encabezado de resultados
print 'type,name,size,i,time,verification'

# experimentos para algoritmos de ordenamiento
test_sort_by_key('mergesort', sizes, fractions, values,keys, runs_for_each_size_and_fraction, mergesort, verifier_sort)
test_sort_by_key('quicksort', sizes, fractions, values,keys, runs_for_each_size_and_fraction, quicksort, verifier_sort)
test_sort_by_key('quicksort-randomizado', sizes, fractions, values,keys, runs_for_each_size_and_fraction, quicksort_randomized, verifier_sort)

