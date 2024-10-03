# generatore di password casuali
# chiedere quanti caratteri special, maiuscole e numeri (se possibile unici)

import random

def introduzione():
    while True:
        procedi = input("Vuoi procedere con la generazione di una password? (s/n): ").strip().lower()
        if procedi == 's':
            return True
        elif procedi == 'n':
            print("Programma terminato. Arrivederci!")
            return False
        else:
            print("Errore: Devi rispondere con 's' o 'n'.")

def genera_password(lunghezza, usa_numeri, usa_caratteri_speciali, lettere_maiuscole, solo_maiuscole, senza_ripetizioni):
    lettere_minuscole = "abcdefghijklmnopqrstuvwxyz"
    lettere_maiuscole_stringa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if lettere_maiuscole or solo_maiuscole else ""

    caratteri_base = lettere_minuscole + lettere_maiuscole_stringa
    
    if usa_numeri:
        caratteri_base += "0123456789"
    if usa_caratteri_speciali:
        caratteri_base += "!@#$%^&*()-_=+[]{}|;:,.<>?/"

    # Controlla se la lunghezza è valida in base ai caratteri disponibili
    if senza_ripetizioni and lunghezza > len(caratteri_base):
        return None  # Lunghezza non valida

    if senza_ripetizioni:
        password = ''.join(random.sample(caratteri_base, lunghezza))
    else:
        password = ''.join(random.choices(caratteri_base, k=lunghezza))

    return password

def ottieni_input():
    lunghezza = 0
    usa_numeri = False
    usa_caratteri_speciali = False
    lettere_maiuscole = False
    solo_maiuscole = False
    senza_ripetizioni = False

    while lunghezza <= 0:
        scelta_lunghezza = input("Vuoi scegliere una lunghezza per la password (s/n)? ").strip().lower()
        if scelta_lunghezza == 's':
            lunghezza_input = input("Inserisci la lunghezza della password: ")
            if lunghezza_input.isdigit():
                lunghezza = int(lunghezza_input)
                if lunghezza <= 0:
                    print("Errore: La lunghezza deve essere un numero positivo.")
            else:
                print("Errore: Inserisci un numero valido.")
        elif scelta_lunghezza == 'n':
            lunghezza = random.randint(8, 16)
            print(f"Lunghezza scelta casualmente: {lunghezza}")
        else:
            print("Errore: Devi rispondere con 's' o 'n'.")

    # Funzione per gestire le opzioni con ripetizione in caso di input non valido
    def chiedi_opzione(messaggio):
        while True:
            risposta = input(messaggio).strip().lower()
            if risposta == 's':
                return True
            elif risposta == 'n':
                return False
            else:
                print("Errore: Devi rispondere con 's' o 'n'.")

    usa_numeri = chiedi_opzione("Vuoi includere numeri? (s/n): ")
    usa_caratteri_speciali = chiedi_opzione("Vuoi includere caratteri speciali? (s/n): ")
    lettere_maiuscole = chiedi_opzione("Vuoi includere lettere maiuscole? (s/n): ")
    
    # Nuova opzione per usare solo lettere maiuscole
    if lettere_maiuscole:
        solo_maiuscole = chiedi_opzione("Vuoi usare solo lettere maiuscole? (s/n): ")

    senza_ripetizioni = chiedi_opzione("Vuoi evitare ripetizioni di caratteri? (s/n): ")

    return lunghezza, usa_numeri, usa_caratteri_speciali, lettere_maiuscole, solo_maiuscole, senza_ripetizioni

# Esecuzione del programma
if introduzione():
    lunghezza, usa_numeri, usa_caratteri_speciali, lettere_maiuscole, solo_maiuscole, senza_ripetizioni = ottieni_input()
    while True:
        password = genera_password(lunghezza, usa_numeri, usa_caratteri_speciali, lettere_maiuscole, solo_maiuscole, senza_ripetizioni)
        
        if password is not None:
            print("Password generata:", password)
            break
        else:
            print("Errore: La lunghezza scelta supera il numero di caratteri unici disponibili.")
else:
    print("Programma terminato. Arrivederci!")