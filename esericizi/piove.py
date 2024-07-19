meteo = input("fuori piove?\n")
if meteo == "sì":
        print("stai a casa")
else:
        umidità =  int(input("qual'è l'umidità rilevata?\n"))
        if umidità >= 70:
            print("stai a casa")
        else:
            print("goditi il sole")
