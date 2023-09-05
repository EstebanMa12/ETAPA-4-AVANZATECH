import random
def mergeSort(array):
    if len(array)>1:
        mid = len(array)//2
        left = array[:mid]
        right = array[mid:]

        mergeSort(left)
        mergeSort(right)

        i=j=k=0

        while i<len(left) and j <len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i+=1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        while i<len(left):
            array[k] = left[i]
            k += 1
            i += 1
        while j<len(right):
            array[k] = right[j]
            i += 1
            j += 1
if __name__ == "__main__":
    from insertionSort import insertionSort
    from quickSort import quickSort
    import timeit
    b = int(input("Ingrese el tamaño de la lista: "))
    array = [random.randint(0,100) for _ in range(b)]
    # print(array)
    # mergeSort(array)
    # print(array) # 4
    print(timeit.timeit(lambda: mergeSort(array), number=1))
    print(timeit.timeit(lambda: insertionSort(array), number=1))
    print(timeit.timeit(lambda: quickSort(array), number=1))