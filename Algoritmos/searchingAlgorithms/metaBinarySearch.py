import random

def meta_binary_search(array, target):
    n = len(array)
    interval_size = n

    while interval_size > 0:
        index = int(min(n - 1, interval_size / 2))
        mid_index = (index + interval_size) // 2
        mid = array[mid_index]
        
        if mid == target:
            return mid_index
        elif mid < target:
            interval_size = (interval_size + index) // 2
        else:
            interval_size = index // 2
    
    return f"No se encontro {target} en la lista"
if __name__ == "__main__":
    b = int(input("Ingrese el tamaño de la lista: "))
    target = int(input("Ingrese el número que desea buscar: "))
    array = sorted([random.randint(0,100) for _ in range(b)])
    print(array)
    print(meta_binary_search(array, target)) # 4