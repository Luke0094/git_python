i = 1
altezza = 6

while i <= altezza:
    j = 0
    while j < i:
        print("1", end="")
        j += 1
    print()
    i += 1


i = 1
# per il numero in alteza di volte, incrementa i ogni volta
while i <= altezza:
    # stampa i volte il sibolo *
    print("*" * i)
    i += 1

i = 1
# per il numero in alteza di volte, incrementa i ogni volta
while i <= 6:
    # stampa i volte il sibolo *
    ramo_albero = " *" * i
    print(ramo_albero.center(30))
    i += 1