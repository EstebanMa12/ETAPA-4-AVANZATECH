import random

def busqueda_lineal(lista, objetivo):
    match = False
    counter =0

    for elemento in lista: # O(n)
        if elemento == objetivo:
            match = True
            break
        counter += 1

    return (match, counter)


if __name__ == '__main__':
    busqueda_lineal()
    # tamano_de_lista = int(input('De que tamano sera la lista? '))
    # objetivo = int(input('Que numero quieres encontrar? '))

    # lista = [random.randint(0, 100) for i in range(tamano_de_lista)]

    # encontrado = busqueda_lineal(lista, objetivo)
    # print(lista)
    # print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')