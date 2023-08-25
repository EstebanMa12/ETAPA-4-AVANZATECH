import time
import sys

def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1

    return respuesta


def factorial_r(n):
    if n == 1:
        return 1

    return n * factorial_r(n - 1)


if __name__ == '__main__':
    n = 2000
    sys.setrecursionlimit(n + 100)

    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(f'Función no recursiva\n Tiempo: {final - comienzo}')

    comienzo = time.time()
    factorial_r(n)
    final = time.time()
    print(f'Función recursiva\n Tiempo: {final - comienzo}')