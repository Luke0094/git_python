import random
seed = random.randint(1, 1000)
random.seed(seed)
print(seed)

somma = 0
tentativi = 10

# per 1000 volte 

i = 0
while i < tentativi:

    # sommo alla variabile soma un numero random tra 1 e 20 compresi
    somma = somma + random.randint(1, 20)
    i += 1
# divido la somma per 1000
media = somma / tentativi
#ottendo il valore atteso (media) di u lancio di dado da 20
print("la media è:", media)


#ottengo il valore atteso (media) di un lancio di dado da 20