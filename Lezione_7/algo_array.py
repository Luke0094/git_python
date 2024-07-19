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

print (max_n([2, 3, 47, 77]))
print (min_n([2, 3, 47, 77]))
print (avg_n([2, 3, 47, 77]))
print(somma_x(2, 4, 5))
