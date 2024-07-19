temperatura = int(input("inserisci la temperatura"))
if temperatura < 30:
    print("che caldo")
else:
    if temperatura < 15:
        print("copriti")
    else:
        print("tutto ok")