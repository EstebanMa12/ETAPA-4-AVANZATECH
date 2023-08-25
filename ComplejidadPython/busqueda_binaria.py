import random
from busqueda_lineal import busqueda_lineal


def busqueda_binaria(lista, comienzo, final, objetivo, counter=0):
    counter +=1
    print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')
    if comienzo > final:
        return False , counter

    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return True , counter
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo, counter=counter)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo, counter=counter)
    


if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano sera la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista = sorted([random.randint(0, 100) for i in range(tamano_de_lista)])

    encontradobinary, cnt_binary = busqueda_binaria(lista, 0, len(lista), objetivo)
    encontrado_linear,cnt_lineal=busqueda_lineal(lista, objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontradobinary else "no esta"} en la lista')
    print(f'Número de iteraciones para la busqueda binaría {cnt_binary}\n Número de iteraciones para la busqueda lineal {cnt_lineal}')