numerouna = (input("scrivi un numero e te lo mostrerò in unario\n"))

print("1" + numerouna)
i = 0


while i < int(numerouna):
    print("1", end="")
    i += 1

i = 0
unario = ""
while i < int(numerouna):
    unario += "1"
    i += 1
    print(unario)
    