# Lab-01. Busqueda lineal y binaria. Ordenamiento por insercion. Experimentos. Analisis de resultados.

# Integrantes:
# Juan Oropeza 15-11041

# extender el limite de la profundidad del stack de recursion
from sys import setrecursionlimit
from sys import path
setrecursionlimit(int(1e6))
path.insert(0, '..')

# importar base
from common.base.basic import read_file
from common.base.test_lab_01 import test_search
from common.base.test_lab_01 import test_sort

from common.base.search import verifier_linear_search
from common.base.search import verifier_binary_search
from common.base.sort import native_sort
from common.base.sort import verifier_sort


########################################################################

def linear_search(A, x):
	for i in range(len(A)):
		if A[i] == x:
			return i
	return -1

def binary_search(A, x):
	start = 0
	end = len(A)
	while start < end:
		mid = (start + end) / 2
		if A[mid] == x:
			return mid
		elif A[mid] < x:
			start = mid + 1
		else:
			end = mid - 1
	if start > len(A) - 1:
		return -1
	else:
		if A[start] == x:		
			return start
		else:
			return -1 

 


def insertion_sort(A):
	for j in range(1,len(A)):
		key = A[j]

		i = j - 1
		while i >= 0 and A[i] > key:
			A[i+1] = A[i]
			i = i - 1
		A[i+1] = key



########################################################################


# leer los datos y preparar variables para correr experimentos
data = read_file('./data/web2')
sizes = [ 2**i for i in range(16) ]
runs_per_each_size = 10
fractions = [ .5, .05, .005, .0005]
runs_per_each_size_and_fraction = 3

# imprimir encabezado de resultados
print 'type,name,size,i,time,verification'

# experimentos para algoritmos de busqueda en arreglos
test_search('linear', sizes, data, runs_per_each_size, linear_search, verifier_linear_search, False)
test_search('binary', sizes, data, runs_per_each_size, binary_search, verifier_binary_search, True)

# experimentos para algoritmos de ordenamiento
test_sort('native', sizes, fractions, data, runs_per_each_size_and_fraction, native_sort, verifier_sort)
test_sort('insertion', sizes[:-1], fractions, data, runs_per_each_size_and_fraction, insertion_sort, verifier_sort)

