from algo_array import *

if max_n([2, 3, 47, 77]) == 77:
    print("Test 1 superato")
else:
    print("test 1 fallito")

if min_n([8, -9, 3]) == 8:
    print("Test 2 superato")
else:
    print("test 2 fallito")

if max_n([]) == 0:
    print("Test 3 superato")
else:
    print("test 3 fallito")

if remove ([1, 2, 3, 4], 1) == [2, 3, 4]:
        print("test 4 superato")
else:
     print("Test 4 fallito")

print (min_n([2, 3, 47, 77]))
print (avg_n([2, 3, 47, 77]))
print(somma_x(2, 4, 5))