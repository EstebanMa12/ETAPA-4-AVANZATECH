import random

def jump_search(array, target):
    n = len(array)
    step = int(n ** 0.5)
    start = 0
    end = step

    while (end < n and array[end] < target):
        print(f"Searching since {array[start]} to end {array[end]}")
        start = end
        end += step
        if end > n - 1:
            end = n
    print(f'Final search since {array[start]} to {array[end]}')
    for i in range(start,end):
        print(array[i])
        if array[i]==target:
            return i
        
    return -1

if __name__ == "__main__":
    b = int(input("Ingrese el tamaño de la lista: "))
    array = sorted([random.randint(0,100) for _ in range(b)])
    print(array)
    target = int(input("Ingrese el número que desea buscar: "))
    print(jump_search(array, target))

