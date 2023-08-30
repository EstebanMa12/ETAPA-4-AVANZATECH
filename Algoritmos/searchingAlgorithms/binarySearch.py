import random
def binarySearch(array, target):
    low = 0; high = len(array) - 1
    counter=0
    while low <= high:
        mid = (low + high)//2
        counter +=1
        if array[mid] == target:
            return mid, counter
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return f"No se encontro {target} en la lista"

if __name__ == "__main__":
    b = int(input("Ingrese el tamaño de la lista: "))
    target = int(input("Ingrese el número que desea buscar: "))
    array = sorted([random.randint(0,100) for _ in range(b)])
    print(array)
    print(binarySearch(array, target)) # 4