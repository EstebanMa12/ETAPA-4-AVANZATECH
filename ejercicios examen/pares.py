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
    sorted_arr = sorted(array)
    low = 0
    high = len(sorted_arr) - 1
    counter = 0
    sum = 0
    while low < high:
        sum = sorted_arr[low] + sorted_arr[high]
        if sum == target:
            print(f"Coincidencia {counter} => {sorted_arr[low]} + {sorted_arr[high]}")
            low +=1
            counter +=1
        elif sum > target:
            high -=1
        else:
            low +=1
    return counter

def findPair3(array, target):
    hash_table = {}
    count = 0
    for number in array:
        complement = target - number
        if complement in hash_table:
            count += hash_table.get(complement, 0)
            print(f"Coincidencia {count} => {number} + {complement}")
        hash_table[number] =  hash_table.get(number,0)+1
    return count

if __name__ == "__main__":
    from random import randint
    array = [5, 4, 4, 2, 1]#[randint(0, 100) for _ in range(10)]
    target = 5 #randint(0, 100)
    print(array)
    print(f"Target: {target}")
    print(f"Numero de coincidencias: {findPair(array, target)}")
    print(f"Numero de coincidencias: {findPair2(array, target)}")
    print(f"Numero de coincidencias: {findPair3(array, target)}")

