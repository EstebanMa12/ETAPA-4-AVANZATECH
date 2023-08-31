def calcMinRun(n):
    """Calcula el tamaño del run minimo"""
    r = 0
    while n >= 64:
        r |= n & 1
        n >>= 1
    return n + r

def insertionSort(arr, start, end):
    """Ordena el array usando insertion sort en el rango [start, end)"""
    if start < 0:
        start = 0
    if end > len(arr):
        end = len(arr)
    for i in range(start + 1, end):
        elem = arr[i]
        j = i - 1
        while j >= start and elem < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = elem

def merge(arr, start, mid, end):
    """Fusiona dos arrays ordenados en uno"""
    if mid == end:
        return
    first = arr[start:mid]
    last = arr[mid:end]
    len1 = mid - start
    len2 = end - mid
    if len1 > len2:
        i = j = k = 0
        while i < len1 and j < len2:
            if first[i] < last[j]:
                arr[start + k] = first[i]
                i += 1
            else:
                arr[start + k] = last[j]
                j += 1
            k += 1
        while i < len1:
            arr[start + k] = first[i]
            k += 1
            i += 1
        while j < len2:
            arr[start + k] = last[j]
            k += 1
            j += 1
    else:
        i = j = k = 0
        while i < len1 and j < len2:
            if last[j] < first[i]:
                arr[start + k] = last[j]
                j += 1
            else:
                arr[start + k] = first[i]
                i += 1
            k += 1
        while i < len1:
            arr[start + k] = first[i]
            k += 1
            i += 1
        while j < len2:
            arr[start + k] = last[j]
            k += 1
            j += 1

def timSort(arr):
    """Ordena el array usando tim sort"""
    n = len(arr)
    minRun = calcMinRun(n)
    for start in range(0, n, minRun):
        end = min(start + minRun, n)
        insertionSort(arr, start, end)
    size = minRun
    while size < n:
        for start in range(0, n, size * 2):
            mid = min(n, start + size)
            end = min(n, mid + size)
            merge(arr, start, mid, end)
        size *= 2

if __name__ == "__main__":
    from random import randint
    tamano_de_lista = int(input('De que tamaño sera la lista? '))
    lista = [randint(0, 100) for i in range(tamano_de_lista)]
    print(lista)
    timSort(lista)
    print(lista)