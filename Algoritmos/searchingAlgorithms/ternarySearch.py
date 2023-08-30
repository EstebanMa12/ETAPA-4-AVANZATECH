import random
def ternary_search(low=0, high=None, target=0, array=[]):
    if high is None:
        high = len(array) - 1

    if low <= high:
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3

        if array[mid1] == target:
            return mid1, 1  # Retorna el índice y el contador actualizado
        if array[mid2] == target:
            return mid2, 1  # Retorna el índice y el contador actualizado

        if target < array[mid1]:
            index, contador = ternary_search(low, mid1 - 1, target, array)
            contador += 1  # Actualiza el contador
            return index, contador
        elif target > array[mid2]:
            index, contador = ternary_search(mid2 + 1, high, target, array)
            contador += 1  # Actualiza el contador
            return index, contador
        else:
            index1, contador1 = ternary_search(low, mid1 - 1, target, array)
            index2, contador2 = ternary_search(mid2 + 1, high, target, array)
            contador = contador1 + contador2 + 1  # Actualiza el contador
            return index1, contador

    return -1, 0 

def ternary_search_iterative(low=0, high=None, target=0, array=[]):
    if high is None:
        high = len(array) - 1 
    while low <= high:
        mid1 = low + (high - low)//3
        mid2 = high - (high - low)//3

        if array[mid1]==target:
            return mid1, 1
        elif array[mid2]==target:
            return mid2, 1
        elif target < array[mid1]:
            high = mid1 -1
        elif target > array[mid2]:
            low  = mid2 + 1
        else:
            low = mid1 + 1
            high = mid2 - 1
    return -1

    pass
if __name__ == "__main__":
    b = int(input("Ingrese el tamaño de la lista: "))
    target = int(input("Ingrese el número que desea buscar: "))
    array = sorted([random.randint(0,100) for _ in range(b)])
    print(array)
    print(ternary_search(target=target, array=array)) # 4
    print(ternary_search_iterative(target=target, array=array)) # 4

