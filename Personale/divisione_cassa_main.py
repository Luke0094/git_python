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