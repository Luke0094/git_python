# si chiede di scrivere 6 numeri tra 1-90
# si confrontano con 6 numeri estratti
# si informa il soggetto di quati e quali numeri ha indovinato
import random
lotteria = []
numeri_utente = []
for i in range(0,6):

    numeri = random.randint(1,91)
    lotteria.append(numeri)

    numeri_usati = int(input("digita 6 numeri scelti da 1 a 90, ogni numero seguito da invio \n"))
    numeri_utente.append(numeri_usati)
    

if numeri_utente == lotteria:
    print("Congratulazioni hai vinto")
else:
    print("mi dispiace riprova")
    print ("i numeri corretti erano" + [lotteria])