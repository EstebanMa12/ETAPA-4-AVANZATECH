def findPair(array, target):
    n = len(array)
    counter = 0
    for i in range(n):
        for j in range(i + 1, n):
            if array[i] + array[j] == target:
                counter +=1
                print(f"Coincidencia {counter} => {array[i]} + {array[j]}")
    return counter

def findPair2(array, target):
    pass

def findPair3(array, target):
    pass

if __name__ == "__main__":
    from random import randint
    array = [5, 4, 3, 2, 1]#[randint(0, 100) for _ in range(10)]
    target = 5 #randint(0, 100)
    print(array)
    print(f"Target: {target}")
    print(f"Numero de coincidencias: {findPair(array, target)}")
