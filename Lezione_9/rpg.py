from mostro import Mostro
from classi import Ladro, Mago, Guerriero
from combattimento import combattimento

mio_pg = Ladro(10,"Beppe", 5,2,2)
mio_mostro = Mostro("Goblin", 10)
mio_mostro2 = Mostro("Mummia", 22)
# mio_mostro.colore = "Nero"
# print(mio_mostro2.colore)


mio_mostro.ruggisci()
mio_mostro2.ruggisci()

cmb = combattimento(mio_pg, mio_mostro)
cmb.combat()
cmb.combat()
cmb.combat()
cmb.attacco.speciale()

