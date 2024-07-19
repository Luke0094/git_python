#esercizio censura

testo = "non mi toglieranno mai il 4° emendamento"
analisi_testo=testo.split()
parole_vietate =["4°", "5°", "emendamento", "non", "legge", "libero", "aiuto",]

for i in range(len(analisi_testo)):
    if analisi_testo[i].lower() in parole_vietate:
        analisi_testo[i] = (len(analisi_testo[i])-2) * "*"

print(" ".join(analisi_testo))


testo_x = "non mi toglieranno mai il 4° emendamento"

parole_censurate = ["4°", "5°", "emendamento", "non", "legge", "libero", "aiuto",]

array_testo = testo.split(" ")
for i in range(0, len(array_testo)):
    parola = array_testo[i].lower()
    parola = parola.replace(".", "") # rimpiazza il punto con ", quindi togliendolo"
    if parola in parole_censurate:
        array_testo[i] = array_testo[i][0] + "*" * (len(array_testo[i]) - 2) + array_testo[i][-1]

print(" ".join(array_testo))