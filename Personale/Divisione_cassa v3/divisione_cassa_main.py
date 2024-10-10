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
            for i, cassa in enumerate(gestore.casse):
                print(f"{i + 1}. {cassa.nome} ({cassa.stato}) - Clienti in coda: {cassa.clienti_in_coda}")

            indice = input("Inserisci il numero della cassa da aprire (1-3), o premi '0' per tornare indietro: ")
            if indice == '' or not indice.isdigit():
                print("Indice cassa non valido.")
                continue
            
            indice = int(indice) - 1
            if indice == -1:
                continue
            gestore.apri_cassa(indice)

        elif scelta == '2':
            numero_clienti = random.randint(1, 20)
            print(f"Aggiungo {numero_clienti} clienti casuali alla coda.")
            gestore.aggiungi_clienti(numero_clienti)

        elif scelta == '3':
            for i, cassa in enumerate(gestore.casse):
                print(f"{i + 1}. {cassa.nome} ({cassa.stato}) - Clienti in coda: {cassa.clienti_in_coda}")

            indice = input("Inserisci il numero della cassa a cui aggiungere i clienti (1-3), o premi '0' per tornare indietro: ")
            if indice == '' or not indice.isdigit():
                print("Indice cassa non valido.")
                continue
            
            indice = int(indice) - 1
            if indice == -1:
                continue
            
            if 0 <= indice < len(gestore.casse):
                numero_clienti = int(input("Inserisci il numero di clienti da aggiungere: "))
                gestore.aggiungi_clienti(numero_clienti, indice)
            else:
                print("Indice cassa non valido.")

        elif scelta == '4':
            for i, cassa in enumerate(gestore.casse):
                print(f"{i + 1}. {cassa.nome} ({cassa.stato}) - Clienti in coda: {cassa.clienti_in_coda}")

            indice_da = input("Inserisci il numero della cassa da cui spostare i clienti (1-3), o premi '0' per tornare indietro: ")
            if indice_da == '' or not indice_da.isdigit():
                print("Indice cassa non valido.")
                continue
            
            indice_da = int(indice_da) - 1
            if indice_da == -1:
                continue
            
            if not (0 <= indice_da < len(gestore.casse)):
                print("Indice cassa non valido.")
                continue

            if gestore.casse[indice_da].clienti_in_coda == 0:
                print("Non ci sono clienti da spostare in questa cassa.")
                continue

            indice_a = input("Inserisci il numero della cassa a cui spostare i clienti (1-3), o premi '0' per annullare: ")
            if indice_a == '' or not indice_a.isdigit():
                print("Indice cassa non valido.")
                continue
            
            indice_a = int(indice_a) - 1
            if indice_a == -1:
                continue

            if indice_da == indice_a:
                print("Impossibile spostare i clienti nella stessa cassa di provenienza.")
                continue

            if not (0 <= indice_a < len(gestore.casse)):
                print("Indice cassa non valido.")
                continue

            numero_clienti = int(input("Inserisci il numero di clienti da spostare: "))
            gestore.sposta_clienti(indice_da, indice_a, numero_clienti)

        elif scelta == '5':
            print("Servendo tutti i clienti in coda...")
            clienti_serviti = 0
            casse_con_clienti = [cassa for cassa in gestore.casse if cassa.clienti_in_coda > 0]
            
            if not casse_con_clienti:
                print("Non ci sono clienti da servire in nessuna cassa.")
            else:
                for cassa in casse_con_clienti:
                    if cassa.stato == "chiusa":
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
                print(f"{i + 1}. {cassa.nome} ({cassa.stato}) - Clienti in coda: {cassa.clienti_in_coda}")
            indice_cassa = input("Inserisci il numero della cassa, o premi '0' per tornare indietro: ")
            if indice_cassa == '' or not indice_cassa.isdigit():
                print("Indice cassa non valido.")
                continue
            
            indice_cassa = int(indice_cassa) - 1
            if indice_cassa == -1:
                continue
            
            if 0 <= indice_cassa < len(gestore.casse):
                cassa_selezionata = gestore.casse[indice_cassa]
                if cassa_selezionata.stato == "chiusa":
                    print(f"La cassa '{cassa_selezionata.nome}' è chiusa. Impossibile servire clienti.")
                elif cassa_selezionata.clienti_in_coda == 0:
                    print("Non ci sono clienti da servire nella cassa selezionata.")
                else:
                    cassa_selezionata.servi_cliente()
                    print("Cliente servito con successo.")
            else:
                print("Indice cassa non valido.")

        elif scelta == '7':
            for i, cassa in enumerate(gestore.casse):
                print(f"{i + 1}. {cassa.nome} ({cassa.stato}) - Clienti in coda: {cassa.clienti_in_coda}")
                
            indice = input("Inserisci il numero della cassa da chiudere (1-3), o premi '0' per tornare indietro: ")
            if indice == '' or not indice.isdigit():
                print("Indice cassa non valido.")
                continue
            
            indice = int(indice) - 1
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
