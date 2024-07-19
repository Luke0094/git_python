def max_n(array):
    massimo = 0
    for item in array:
        if massimo < item:
            massimo = item
    return massimo

def min_n(array):
    minimo = array[0]
    for item in array:
        if minimo > item:
            minimo = item
    return minimo

def somma_n(array):
    somma = 0
    for item in array:
        somma += item
    return somma

def avg_n(array):
    return somma_n(array) / len(array)

def somma_array(array):
    somma_x = 0
    for item in array:
        somma_x += item
    return somma_x

def somma_x(*numeri):
    return somma_array(list(numeri))

#cancella dall'array il primo elemento trovato uguale a x
def remove(array, x):
    for i in range(len(array)):
        print(array[index], x)
        if [i] == x:
            del array[i]
            print[i]
            del array[i]
            print (x)
            break
    return array

#reverse 
def reverse(array):
    return

def index(array, x):
    return 0

def concatenate(array, array2):
    return 0


print (max_n([2, 3, 47, 77]))
print (min_n([2, 3, 47, 77]))
print (avg_n([2, 3, 47, 77]))
print(somma_x(2, 4, 5))
