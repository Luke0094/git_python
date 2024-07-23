# pizza small 5€ medium 7€ large 10€
# scelta di mozzarella bufala + 2 euro per small e mudium + 3 large
# scelta ingredienti + 1 euro a ingrdiente
# consegna a casa si / no + 2 euro
# gratis per large
# totale

small = 5
medium = 7
large = 10
mozzarella_bufala = 2
ingredienti = []
max_ingredienti = 5
spedizione_small = 2
spedizione_medium = 2
spedizione_large = 0
costo_totale = 0


print("buongiorno, i nostro servizi sono:\n pizza small 5€\n pizza medium 7€\n pizza lareg 10€\n ogni ingrdiente aggiunto costerà 1 euro, in più nel caso di mozzarella di bufala 2 euro\n consegna a 2 euro, gratis per large \n")

dimensione_pizza = input("Quale dimensione pizza desideri? \n")
print("hai selezionato " + dimensione_pizza)
prog_dimensione = input("vuoi aggiungere qualche ingrediente particolare? \n")
if prog_dimensione == "no":
    print("Il tuo carrello contiene " + prog_dimensione)
    if prog_dimensione == small or medium:
        print("il tuo costo totale è di " + costo_totale)
    else:
        print("il tuo costo totale è di " + costo_totale)
    

if prog_dimensione == "sì":
    
    while ingredienti < max_ingredienti:
        ingredienti = input(list("Per favore inserisci la tua lista di ingredienti extra (max 5) \n"))
        if ingredienti == "mozzarella bufala":
            costo_totale =+ 2
        else:
            costo_totale =+ 1

else:
    print("Scusa non ho capito \n")

