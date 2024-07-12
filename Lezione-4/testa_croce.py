import random


scelta = input("testa o croce\n")

tiro = random.randint(0,2)

if tiro == 1:
    print("pc : testa")
else:
    print("pc : croce")

if (scelta =="testa" and tiro==1) or (scelta=="croce" and tiro==0):
    print("hai vinto")
elif scelta != "testa" or "croce":
    print("la scelta è solo testa o croce!")
else:
    print("hai perso")