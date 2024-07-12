import random

tiro = random.randint(1, 10)
partite_iniziali = 0
partite_massime = 5
while partite_iniziali < partite_massime:
    
    partite_iniziali += 1
    scelta = int(input("alto o basso? (Inserisci un numero tra 1 e 10)\n"))

    if tiro >= int(scelta):
        print(tiro)
        print("basso!")
    elif tiro == int(scelta):
        print(tiro)
        print("patta!")
    else:
        print(tiro)
        print("alto!")
    

