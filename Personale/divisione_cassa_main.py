import random
from divisione_cassa import GestoreCasse

def main():
    gestore = GestoreCasse()
    
    # Apertura iniziale della Cassa 1
    gestore.apri_cassa(0)

    while True:
        print("\nMenu:")
        print("1. Apri cassa")
        print("2. Aggiungi clienti casuali")
        print("3. Aggiungi manualmente clienti alla coda")
        print("4. Sposta clienti da una cassa all'altra")
        print("5. Servire tutti i clienti in coda")
        print("6. Servire un cliente")
        print("7. Chiudi cassa")
        print("8. Visualizza stato casse")
        print("9. Visualizza incassi per cassa")
        print("10. Esci")

        scelta = input("Seleziona un'opzione: ")

        if scelta == '1':
            indice = int(input("Inserisci il numero della cassa da aprire (1-3): ")) - 1
            gestore.apri_cassa(indice)

        elif scelta == '2':
            numero_clienti = random.randint(1, 20)
            print(f"Aggiungo {numero_clienti} clienti casuali alla coda.")
            gestore.aggiungi_clienti(numero_clienti)

        elif scelta == '3':
            numero_clienti = int(input("Inserisci il numero di clienti da aggiungere: "))
            indice = int(input("Inserisci il numero della cassa a cui aggiungere i clienti (1-3), o 0 per la prima disponibile: ")) - 1
            if indice == -1:
                gestore.aggiungi_clienti(numero_clienti)
            else:
                gestore.aggiungi_clienti(numero_clienti, indice)

        elif scelta == '4':
            indice_da = int(input("Inserisci il numero della cassa da cui spostare i clienti (1-3): ")) - 1
            indice_a = int(input("Inserisci il numero della cassa a cui spostare i clienti (1-3): ")) - 1
            numero_clienti = int(input("Inserisci il numero di clienti da spostare: "))
            gestore.sposta_clienti(indice_da, indice_a, numero_clienti)

        elif scelta == '5':
            print("Servendo tutti i clienti in coda...")
            clienti_serviti = 0
            while gestore.coda_clienti > 0:
                if gestore.serve_cliente():
                    clienti_serviti += 1
                else:
                    print(f"Impossibile servire altri clienti. {clienti_serviti} clienti sono stati serviti.")
                    break
            if clienti_serviti == gestore.coda_clienti:
                print("Tutti i clienti in coda sono stati serviti.")

        elif scelta == '6':
            print("Seleziona una cassa per servire un cliente:")
            for i, cassa in enumerate(gestore.casse):
                stato = "chiusa" if not cassa.aperta else "aperta"
                clienti_in_coda = cassa.clienti_in_coda
                
                if clienti_in_coda >= 1:
                    print(f"{i + 1}. {cassa.nome_cassiere} ({stato}) - Clienti in coda: {clienti_in_coda}")
                elif clienti_in_coda == 1:
                    print(f"{i + 1}. {cassa.nome_cassiere} ({stato}) - 1 cliente in coda")
                else:
                    print(f"{i + 1}. {cassa.nome_cassiere} ({stato}) - Nessun cliente in coda")

            indice_cassa = int(input("Inserisci il numero della cassa: ")) - 1

            if 0 <= indice_cassa < len(gestore.casse):
                cassa_selezionata = gestore.casse[indice_cassa]
                if not cassa_selezionata.aperta:
                    print(f"La cassa '{cassa_selezionata.nome_cassiere}' è chiusa. Impossibile servire clienti.")
                else:
                    if cassa_selezionata.avanti_cliente():
                        print("Cliente servito con successo.")
                    else:
                        print("Impossibile servire il cliente dalla cassa selezionata.")
            else:
                print("Selezione cassa non valida.")

        elif scelta == '7':
            indice = int(input("Inserisci il numero della cassa da chiudere (1-3): ")) - 1
            gestore.chiudi_cassa(indice)

        elif scelta == '8':
            gestore.visualizza_stato()

        elif scelta == '9':
            gestore.visualizza_incassi()

        elif scelta == '10':
            print("Uscita dal programma.")
            break

        else:
            print("Scelta non valida, riprova.")

if __name__ == "__main__":
    main()



















"""
from divisione_cassa import GestoreCasse

def main():
    gestore = GestoreCasse()
    
    # Apertura iniziale della Cassa 1
    gestore.apri_cassa(0)

    while True:
        print("\nMenu:")
        print("1. Aggiungi clienti alla coda")
        print("2. Chiudi cassa")
        print("3. Serve cliente")
        print("4. Visualizza stato casse")
        print("5. Esci")

        scelta = input("Seleziona un'opzione: ")

        if scelta == '1':
            numero_clienti = int(input("Inserisci il numero di clienti da aggiungere: "))
            gestore.aggiungi_clienti(numero_clienti)

        elif scelta == '2':
            indice = int(input("Inserisci il numero della cassa da chiudere (1-3): ")) - 1
            gestore.chiudi_cassa(indice)

        elif scelta == '3':
            gestore.serve_cliente()

        elif scelta == '4':
            gestore.visualizza_stato()

        elif scelta == '5':
            print("Uscita dal programma.")
            break

        else:
            print("Scelta non valida, riprova.")

if __name__ == "__main__":
    main()
"""
