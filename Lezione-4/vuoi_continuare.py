print("faccio qualcosa")
print("Vuoi continuare?\n")
risposta = "no"
risposta = input("Si o no?")

while risposta != "si" and risposta != "no":
    risposta = input("si o no?\n")


prima_volta = True
risposta = "si"

while risposta == "si" or prima_volta:
    risposta = input("si o no?\n")
    print("si o no?")