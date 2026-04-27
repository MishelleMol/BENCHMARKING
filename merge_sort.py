

def merge_sort(arr: list) -> list:  # Función principal de merge sort
    n = len(arr)  # Obtiene el tamaño del arreglo

    if n <= 1:  # Caso base: si el arreglo tiene 1 o 0 elementos
        return arr  # Ya está ordenado

    mid = n // 2  # Encuentra la mitad del arreglo

    left = merge_sort(arr[:mid])   # Ordena recursivamente la mitad izquierda
    right = merge_sort(arr[mid:])  # Ordena recursivamente la mitad derecha

    return merge(left, right)  # Combina ambas mitades ordenadas


def merge(left: list, right: list) -> list:  # Función que une dos listas ordenadas
    result = []  # Lista donde se guardará el resultado final
    i = 0  # Índice para recorrer la lista izquierda
    j = 0  # Índice para recorrer la lista derecha

    while (i < len(left)) and (j < len(right)):  # Mientras haya elementos en ambas listas
        if left[i] <= right[j]:  # Compara los elementos actuales
            result.append(left[i])  # Agrega el menor
            i += 1  # Avanza en la lista izquierda
        else:
            result.append(right[j])  # Agrega el menor
            j += 1  # Avanza en la lista derecha

    result.extend(left[i:])   # Agrega los elementos restantes de la izquierda
    result.extend(right[j:])  # Agrega los elementos restantes de la derecha

    return result  # Retorna la lista combinada y ordenada


