 # matrici  1 0 0 2
 #          3 0 2 3
 #          4 1 0 0

matrice = [[1,0,0,2], [3,0,2,3], [4,1,0,0]]

# stampa classica
for i in range (0,len(matrice)):
    for j in range(0, len(matrice[i])):
        print(matrice[i][j])

# stampa moderna
for riga in matrice: # numero di righe
    for numero in riga: # numero di colonner
        print(numero)

# diagonale
for i in range(0, len(matrice)):
    matrice[i][i] = 6
print(matrice)

# colonne
for i in range(0, len(matrice)):
    matrice[i][3] = 1

print(matrice)

def stampa_matrice(matrix):
    for riga in matrix:
        for elemento in riga:
            print(elemento, end=" ")
        print()
    print()

# stampa_matrice([[1,0,0], [8,0,2], [1,0,2]])
# stampa_matrice([[1,4,4], [8,5,2], [1,0,2]])

# matrice_quadrata = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]

# esercizio
# daro un numero intero, genere una matrice di quelle dimensioni.
# per esempio dato 4, genera: 1 2 3 4
#                             5 6 7 8
#                             9 10 11 12
#                             13 14 15 16

num = int(input("Inserisci numero: \n"))
matrice_x = []
conta = 1

for indice_riga in range(num):
#genero riga incrementando ogni volta conta
    riga = []
    for indice_elemento in range(num):
        riga.append(conta)
        conta += 1
    matrice_x.append(riga)

# stampo la matrice
for riga in matrice_x:
    for elemento in matrice_x:
        for elemento in riga:
            print(elemento, end=" ")
    print()
print()

#import math
# 
#lato = int(input("dammi un numero: \n"))
#altezza = lato
#matrice_y = []
#
#while lato > 0:
#    matrice_y.append(int(lato))
#    lato = lato -1
#
#    if lato < 0:
#        print("dimmi un valore valido: \n")
#        lato = int(input)("scrivi il valore in mumeri interi positivi")
#
#print(matrice_y)
#
#lun_riga = int(math.sqrt(lato))

#while lun_riga > 0
#riga= []
#
#   for i in matrice_y:
#       riga=[]
#       for j in matrice_y
#           riga.append(int(j))
#           lun_riga = lun_riga -1
#
#matrice_y.append(riga)
#print(matrice_y)

