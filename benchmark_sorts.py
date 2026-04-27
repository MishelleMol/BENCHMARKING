''' Benchmark for Bubble Sort and Merge Sort '''

from bubble_sort import bubble_sort
from merge_sort import merge_sort


def my_benchmark(option):
    n = 2000 #Tamaño del arreglo de prueba
    arr_test = [num for num in range(n, 0, -1)] #Crea un arreglo en orden descendente
    option(arr_test.copy()) #Ejecuta el algoritmo recibido usando una copia del arreglo


def test_bubble_sort(benchmark): #Test que mide el rendimiento de Bubble sort
    benchmark.pedantic( #benchmark con config personalizado
        my_benchmark, #Función que se va medir
        args=(bubble_sort,), #Envía bubble a bench
        rounds=5, #prueba 5 veces
        iterations=3 #Se itera 3 veces 
    )


def test_merge_sort(benchmark): #Test que mide el rendimiento de merge sort
    benchmark.pedantic( #benchmark con configuración personalizado
        my_benchmark, #función que se va a medir
        args=(merge_sort,), #envía merge a bench 
        rounds=5, #prueba 5 veces
        iterations=3  #Itera 3 veces
    )