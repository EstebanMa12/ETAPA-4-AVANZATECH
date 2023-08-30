import random
from binarySearch import binarySearch 

def interpolationSearch(array, target):
    low = 0
    high = len(array) - 1
    while low <= high and target >= array[low] and target <= array[high]:
        if low == high:
            if array[low] == target:
                return low
            return -1

        position = low + int(((float(high - low) / (array[high] - array[low])) * (target - array[low])))
        print(f"Actual position: {position} in number: {array[position]}")

        if array[position] == target:
            return position

        if array[position] < target:
            low = position + 1
        else:
            high = position - 1
    return -1

if __name__ == "__main__":
    b = int(input("Ingrese el tamaño de la lista: "))
    array = sorted([random.randint(0,100) for _ in range(b)])
    print(array)
    target = int(input("Ingrese el número que desea buscar: "))
    print(interpolationSearch(array, target))
    idx, bucles = binarySearch(array, target)
    print(f"El indice es {idx} y el numero de bucles con binarySearch es {bucles}")
