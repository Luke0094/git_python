import random

tiro = random.randint(0,100 +1)
scelta = 0

while tiro != scelta:

    user = int(input("scegli un numero compreso tra 1 e 100 \n"))
    
    if tiro == user:
        print("esatto!")
        break

    if user < tiro:
        print("acqua")

    if user > tiro:
        print("fuoco")
    