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
        caratteri_base += "!@#$%^&*()-_=+[]{}|;:,.<>?"

    if senza_ripetizioni and lunghezza > len(caratteri_base):
        return None  # Lunghezza non valida

    if senza_ripetizioni:
        password = ''.join(random.sample(caratteri_base, lunghezza))
    else:
        password = ''.join(random.choices(caratteri_base, k=lunghezza))

    return password

def chiedi_opzione(messaggio):
    while True:
        risposta = input(messaggio + " (s/n per continuare, r per tornare indietro, q per ricominciare): ").strip().lower()
        if risposta == 's':
            return True
        elif risposta == 'n':
            return False
        elif risposta == 'r':
            return 'r'  # Torna indietro
        elif risposta == 'q':
            return 'q'  # Ricomincia
        else:
            print("Errore: Risposta non valida.")

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
            lunghezza_input = input("Inserisci la lunghezza della password (o 'q' per ricominciare): ")
            if lunghezza_input.lower() == 'q':
                return None  # Ricomincia l'operazione
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

    while True:
        usa_numeri = chiedi_opzione("Vuoi includere numeri?")
        if usa_numeri == 'r':
            continue
        if usa_numeri == 'q':
            return None  # Ricomincia

        usa_caratteri_speciali = chiedi_opzione("Vuoi includere caratteri speciali?")
        if usa_caratteri_speciali == 'r':
            continue
        if usa_caratteri_speciali == 'q':
            return None  # Ricomincia

        lettere_maiuscole = chiedi_opzione("Vuoi includere lettere maiuscole?")
        if lettere_maiuscole == 'r':
            continue
        if lettere_maiuscole == 'q':
            return None  # Ricomincia

        if lettere_maiuscole:
            solo_maiuscole = chiedi_opzione("Vuoi usare solo lettere maiuscole?")
            if solo_maiuscole == 'r':
                continue
            if solo_maiuscole == 'q':
                return None  # Ricomincia

        senza_ripetizioni = chiedi_opzione("Vuoi evitare ripetizioni di caratteri?")
        if senza_ripetizioni == 'r':
            continue
        if senza_ripetizioni == 'q':
            return None  # Ricomincia

        break

    return lunghezza, usa_numeri, usa_caratteri_speciali, lettere_maiuscole, solo_maiuscole, senza_ripetizioni

# Esecuzione del programma
if introduzione():
    while True:
        input_params = ottieni_input()
        if input_params is None:
            print("Operazione annullata. Tornando all'inizio...")
            continue
        
        lunghezza, usa_numeri, usa_caratteri_speciali, lettere_maiuscole, solo_maiuscole, senza_ripetizioni = input_params
        
        while True:
            password = genera_password(lunghezza, usa_numeri, usa_caratteri_speciali, lettere_maiuscole, solo_maiuscole, senza_ripetizioni)
            
            if password is not None:
                print("Password generata:", password)
                break
            else:
                print("Errore: La lunghezza scelta supera il numero di caratteri unici disponibili.")

        if not chiedi_opzione("Vuoi generare un'altra password?"):
            print("Programma terminato. Arrivederci!")
            break
else:
    print("Programma terminato. Arrivederci!")
