# Instogramma


# data ad esempio la lista [3,4,5,5,2], la funione dovrà riprodurre questa sequenza

# ***
# ****
# *****
# *****
# **

arr = [3,4,5,5,2]
for i in range(0,len(arr)):
    print (arr[i]*"*")

print("next")

dati = [3,4,5,5,2]
for dato in dati:
    for _ in range(0,dato):
        print("*", end="")

print("next")


### i 3 bicchieri 
# dato un array e n scambia una volta i bicchieri

import random

def scambia_due_elementi(bicchieri):
    el1 = random.randint(0,len(bicchieri))
    el2 = random.randint(0,len(bicchieri))
    aux = bicchieri[el1]
    bicchieri[el1] = bicchieri[el2]
    bicchieri[el2] = aux
    print(el1,el2)

my_bicchieri = [True,False,False]
scambia_due_elementi(my_bicchieri)
print(my_bicchieri)

print("next")

my_bicchieri = [True,False,False]
def scambia_shuffle(oggetti):
    random.shuffle(oggetti)
scambia_shuffle (my_bicchieri)
print(my_bicchieri)
