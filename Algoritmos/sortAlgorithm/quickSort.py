import random
def partition(array, low, high):
    i = (low - 1)  # index of smaller element
    pivot = array[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or equal to pivot
        if array[j] <= pivot:

            # increment index of smaller element
            i = i + 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return (i + 1)

def quickSort(array, low =0, high=None):
    if high is None:
        high = len(array) - 1
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)
    return array
if __name__ == "__main__":
    b = int(input("Ingrese el tamaño de la lista: "))
    array = [random.randint(0,100) for _ in range(b)]
    print(array)
    print(quickSort(array)) # 4