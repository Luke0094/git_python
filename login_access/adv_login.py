import getpass
import time

Tentativi_iniziali = 0
Tentativi_Massimi = 3
Tempo_Iniziale = 10
Incremento_Tempo = 5

print("Buongiorno!\n")

while Tentativi_iniziali < Tentativi_Massimi:

    login = input("Inserisci il tuo nome utente:\n")
    pw = getpass.getpass("Digita la tua password:\n")
    
    from login_info import * 
    if login == Login_upper or Login_lower and pw == Password:
        print("Bentornato " + Login_upper + "!\n")
        print("Come posso aiutarti?\n")
        break;
    
    else:
        Tentativi_iniziali += 1
        tentativi_rimasti = Tentativi_Massimi - Tentativi_iniziali
        print("Il tuo nome utente o la password non sono corretti, riprova.\n")
        print("Tentativi rimasti: " + str(tentativi_rimasti) + "\n")

        if Tentativi_iniziali >= Tentativi_Massimi:
            print("Hai esaurito i tuoi tentativi.\nIl terminale è stato bloccato, riprova tra:\n")
            
            for x in range(Tempo_Iniziale, 0, -1):
                secondi = x % 60
                minuti = int(x / 60) % 60
                ore = int(x / 3600)
                print(f"{ore:02}:{minuti:02}:{secondi:02}")
                time.sleep(1)

                Tempo_Iniziale += Incremento_Tempo

            Tentativi_iniziali = 0      