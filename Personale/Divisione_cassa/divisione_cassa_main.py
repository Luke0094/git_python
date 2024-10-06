import random
from divisione_cassa import GestoreCasse

def main():
    gestore = GestoreCasse()
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
        print("9. Esci")

        scelta = input("Seleziona un'opzione: ")
        
        if scelta == '1':
            indice = int(input("Inserisci il numero della cassa da aprire (1-3), o premi '0' per tornare indietro: ")) - 1
            if indice == -1:
                continue
            gestore.apri_cassa(indice)

        elif scelta == '2':
            numero_clienti = random.randint(1, 20)
            print(f"Aggiungo {numero_clienti} clienti casuali alla coda.")
            gestore.aggiungi_clienti(numero_clienti)

        elif scelta == '3':
            for i, cassa in enumerate(gestore.casse):
                stato = "chiusa" if not cassa.aperta else "aperta"
                clienti_in_coda = cassa.clienti_in_coda
                print(f"{i + 1}. {cassa.nome} ({stato}) - Clienti in coda: {clienti_in_coda}")
            indice = int(input("Inserisci il numero della cassa a cui aggiungere i clienti (1-3), o premi '0' per tornare indietro: ")) - 1
            if indice == -1:
                continue
            elif 0 <= indice < len(gestore.casse):
                numero_clienti = int(input("Inserisci il numero di clienti da aggiungere: "))
                gestore.aggiungi_clienti(numero_clienti, indice)
            else:
                print("Selezione cassa non valida.")


        elif scelta == '4':
            for i, cassa in enumerate(gestore.casse):
                stato = "chiusa" if not cassa.aperta else "aperta"
                clienti_in_coda = cassa.clienti_in_coda
                print(f"{i + 1}. {cassa.nome} ({stato}) - Clienti in coda: {clienti_in_coda}")
            indice_da = int(input("Inserisci il numero della cassa da cui spostare i clienti (1-3), o premi '0' per tornare indietro: ")) - 1
            if indice_da == -1:
                continue
            else:
                indice_a = int(input("Inserisci il numero della cassa a cui spostare i clienti (1-3), o premi '0' per annullare: ")) - 1
                if indice_a == -1:
                    continue
                else:
                    numero_clienti = int(input("Inserisci il numero di clienti da spostare: "))
                    if 0 <= indice_da < len(gestore.casse) and 0 <= indice_a < len(gestore.casse):
                        gestore.sposta_clienti(indice_da, indice_a, numero_clienti)
                    else:
                        print("Selezione cassa non valida.")

        elif scelta == '5':
            print("Servendo tutti i clienti in coda...")
            clienti_serviti = 0
            casse_con_clienti = [cassa for cassa in gestore.casse if cassa.clienti_in_coda > 0]
            
            if not casse_con_clienti:
                print("Non ci sono clienti da servire in nessuna cassa.")
            else:
                for cassa in casse_con_clienti:
                    if not cassa.aperta:
                        print(f"La cassa '{cassa.nome}' è chiusa. Impossibile servire {cassa.clienti_in_coda} clienti in coda.")
                    else:
                        while cassa.clienti_in_coda > 0:
                            cassa.servi_cliente()
                            clienti_serviti += 1
                
                if clienti_serviti > 0:
                    print(f"{clienti_serviti} clienti sono stati serviti.")
                else:
                    print("Nessun cliente è stato servito. Tutte le casse con clienti sono chiuse.")

        elif scelta == '6':
            print("Seleziona una cassa per servire un cliente:")
            for i, cassa in enumerate(gestore.casse):
                stato = "chiusa" if not cassa.aperta else "aperta"
                clienti_in_coda = cassa.clienti_in_coda
                print(f"{i + 1}. {cassa.nome} ({stato}) - Clienti in coda: {clienti_in_coda}")
            indice_cassa = int(input("Inserisci il numero della cassa, o premi '0' per tornare indietro: ")) - 1
            if indice_cassa == -1:
                continue
            if 0 <= indice_cassa < len(gestore.casse):
                cassa_selezionata = gestore.casse[indice_cassa]
                if not cassa_selezionata.aperta:
                    print(f"La cassa '{cassa_selezionata.nome}' è chiusa. Impossibile servire {cassa_selezionata.clienti_in_coda} clienti in coda.")
                elif cassa_selezionata.clienti_in_coda == 0:
                    print("Non ci sono clienti da servire nella cassa selezionata.")
                else:
                    cassa_selezionata.servi_cliente()
                    print("Cliente servito con successo.")
            else:
                print("Selezione cassa non valida.")

        elif scelta == '7':
            indice = int(input("Inserisci il numero della cassa da chiudere (1-3), o premi '0' per tornare indietro: ")) - 1
            if indice == -1:
                continue
            gestore.chiudi_cassa(indice)

        elif scelta == '8':
            print("\nStato attuale delle casse:")
            gestore.visualizza_stato()
            gestore.visualizza_riepilogo()
            
        elif scelta == '9':
            print("Uscita dal programma.")
            break
        else:
            print("Scelta non valida, riprova.")

if __name__ == "__main__":
    main()