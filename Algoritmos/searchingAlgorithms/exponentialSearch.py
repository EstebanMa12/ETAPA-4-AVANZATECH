import random
from binarySearch import binarySearch

def exponentialSearch(array, target):
    n = len(array)
    if n == 0:
        return -1
 
    # Find range for binary search by repeatedly doubling i
    i = 1
    while i < n and array[i] < target:
        i *= 2
 
    # Perform binary search on the range [i/2, min(i, n-1)]
    left = i // 2
    right = min(i, n-1)
 
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    b = int(input("Ingrese el tamaño de la lista: "))
    array = sorted([random.randint(0,100) for _ in range(b)])
    print(array)
    target = int(input("Ingrese el número que desea buscar: "))
    print(exponentialSearch(array, target))
    idx, bucles = binarySearch(array, target)
    print(f"El indice es {idx} y el numero de bucles con binarySearch es {bucles}")


