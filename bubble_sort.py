"Bubble sort basic implementation with benchmarking"

def bubble_sort(arr: list) -> list: #Recibe una lista y la devulve ordenada
    n = len(arr) #Tamaño de la lista

    for _ in range(n): #Recorre la lista n veces 
        for j in range(n - 1): #Recorre desde 0 hasta n-2
            if arr[j] > arr[j + 1]: #Compara el elemnto con el siguiente
                arr[j], arr[j + 1] = arr[j + 1], arr[j] #Los intercambia si están desordenados 

    return arr #Devuelve el array ordenado


