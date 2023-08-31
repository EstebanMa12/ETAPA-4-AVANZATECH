import random 

def insertionSort(lista):
    for i in range(1, len(lista)):
        key = lista[i]

        j = i-1
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key

if __name__ == "__main__":
    tamano_de_lista = int(input('De que tamaño sera la lista? '))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    print(lista)

    insertionSort(lista)
    print(lista)