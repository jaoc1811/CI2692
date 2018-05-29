<table>
	<tr>
		<th colspan="2" style="text-align:center">
			<img src="http://www.usb.ve/conocer/corporativa/archivos/logos/logo/logo.gif" width="64" height="43"><br/>
			Universidad Sim&oacute;n Bol&iacute;var<br/>
			Departamento de Computaci&oacute;n y Tecnolog&iacute;a de la Informaci&oacute;n<br/>
			Laboratorio de Algoritmos y Estructuras de Datos II (CI 2692)
	</tr>
	<tr>
		<th scope="row">Asignaci&oacute;n:</th>
		<td style="text-align:right">Laboratorio 4</td>
	</tr>
	<tr>
		<th scope="row">Modalidad:</th>
		<td style="text-align:right">Individual</td>
	</tr>
	<tr>
		<th scope="row">Ponderación:</th>
		<td style="text-align:right">2%</td>
	</tr>
	<tr>
		<th scope="row">Asignado:</th>
		<td style="text-align:right">Jueves, 17 de mayo de 2018 (sem 4)</td>
	</tr>
	<tr>
		<th scope="row">Entrega:</th>
		<td style="text-align:right">Sábado, 19 de mayo de 2018 (sem 4)</td>
	</tr>
</table>

### Lab-04: Ordenamiento por claves

#### Objetivos:

1. Adaptar algoritmos de ordenamiento para ordenar un arreglo según los valores de otro

Cada grupo debe entregar el c&oacute;digo implementado haciendo commit 
en el repositorio.

Todos los procedimientos se deben implementar dentro de la plantilla `lab_04.py` 
en la parte del archivo prevista para ello. Las *firmas* de cada procedimiento son las siguientes:

```
def mergesort(values, sortBy):
def quicksort_rec(values, sortBy, p, r, partition_function):
```
donde `values` y `sortBy` son arrays.

Todos los algoritmos se eval&uacute;an de forma *autom&aacute;tica* sobre fuentes
de datos provistas y se generan estad&iacute;sticos de tiempo de ejecuci&oacute;n.
Una vez que se hayan implementado los algoritmos, los experimentos se ejecutan desde
el *shell* de una de las siguiente formas:

```
python lab_04.py > data.csv
python lab_04.py | tee data.csv
```

La primera forma *redirecciona* la salida de la ejecuci&oacute;n al archivo ```data.csv```.
La segunda forma utiliza el programa ```tee``` de unix para mostrar por pantalla la salida y
redireccionarla al archivo ```data.csv```.

Luego usamos el programa estad&iacute;stico R para generar gr&aacute;ficas del tiempo 
de corrida y error:

```
R --no-save < common/plots/plot_lab_04.R
```

Se genera 1 gr&aacute;ficas 

#### Ordenamiento por claves
El ordenamiento por claves se refiere a ordenar un arreglo según los valores de otro. Por ejemplo, si se tienen dos arreglos:
|Pizza	|preferencia|
|-------|-----------|
|Anchoas	|10|
|Cuatro estaciones	|2|
|Cuatro quesos	|5|
|Hawaiana	|8|
|Margarita	|7|
|Meat Lovers	|3|
|Pepperoni	|4|
|Primavera	|6|
|Suprema	|1|
|Vegetariana	|9

Se desea obtener el arreglo pizzas ordenado según el arreglo preferencia, es decir
|Pizza	|preferencia|
|-------|-----------|
|Suprema	|1|
|Cuatro estaciones|2|
|Meat lovers|3|
|Pepperoni|4|
|Cuatro quesos|5|
|Primavera|6|
|Margarita|7|
|Hawaiana|8|
|Vegetariana|9|
|Anchoas	|10|

Esto requiere modificar los algoritmos de búsqueda pedidos para intercambiar las posiciones correspondientes en ambos arreglos en cada swap.

#### Archivo de entrada:
Se proporciona un solo archivo de entrada en ``data/cursos.txt``, el cual indica, para cada sección
de cada curso de esta década, en qué trimestre se abrió. Los datos se cargan en dos arreglos
(código y trimestre). Se espera que su algoritmo sea capaz de ordenarlos por trimestre.

Observe que este conjunto de datos tendrá un gran número de valores repetidos, por lo que es
necesario trabajar con pivotes de dos valores.

