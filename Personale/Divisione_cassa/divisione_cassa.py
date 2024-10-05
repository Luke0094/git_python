import random

class Cassa:
    def __init__(self, nome_cassiere, posizione, aperta=False):
        self.nome_cassiere = nome_cassiere
        self.posizione = posizione
        self.aperta = aperta
        self.clienti_in_coda = 0
        self.incasso = 0
        self.clienti_gestiti = 0

    def apri(self):
        if not self.aperta:
            self.aperta = True
            print(f"La cassa '{self.nome_cassiere}' è ora aperta.")

    def chiudi(self):
        if self.aperta:
            self.aperta = False
            print(f"La cassa '{self.nome_cassiere}' è ora chiusa.")

    def avanti_cliente(self):
        if self.aperta and self.clienti_in_coda > 0:
            self.clienti_in_coda -= 1
            incasso_cliente = random.randint(5, 20)
            self.incasso += incasso_cliente
            self.clienti_gestiti += 1
            print(f"Un cliente è stato servito alla cassa '{self.nome_cassiere}'. Clienti in coda: {self.clienti_in_coda}. Incasso: {incasso_cliente} euro.")
            return True
        return False

    def aggiungi_clienti(self, numero):
        self.clienti_in_coda += numero
        print(f"{numero} clienti aggiunti alla coda della cassa '{self.nome_cassiere}'. Clienti in coda: {self.clienti_in_coda}.")

    def visualizza_incasso(self):
        print(f"Incasso totale alla cassa '{self.nome_cassiere}': {self.incasso} euro.")

class GestoreCasse:
    def __init__(self):
        self.casse = [Cassa(f"Cassa {i + 1}", i + 1) for i in range(3)]
        self.coda_clienti = 0
        self.avviso_casse_chiuse_inviato = False

    def apri_cassa(self, indice):
        if 0 <= indice < len(self.casse):
            cassa = self.casse[indice]
            if not cassa.aperta:
                cassa.apri()
                print(f"La cassa '{cassa.nome_cassiere}' è stata aperta.")
            else:
                print(f"La cassa '{cassa.nome_cassiere}' è già aperta.")
        else:
            print("Indice cassa non valido.")

    def chiudi_cassa(self, indice):
        if 0 <= indice < len(self.casse):
            cassa = self.casse[indice]
            if cassa.aperta:
                clienti_da_ridistribuire = cassa.clienti_in_coda
                print(f"Chiudendo la cassa '{cassa.nome_cassiere}'. Clienti da ridistribuire: {clienti_da_ridistribuire}.")
                cassa.chiudi()
                self.ridistribuisci_clienti(clienti_da_ridistribuire)
            else:
                print(f"La cassa '{cassa.nome_cassiere}' è già chiusa.")
        else:
            print("Indice cassa non valido.")

    def ridistribuisci_clienti(self, numero_clienti):
        casse_aperte = [cassa for cassa in self.casse if cassa.aperta]
        if not casse_aperte:
            print("Nessuna cassa aperta. Impossibile ridistribuire i clienti.")
            self.coda_clienti += numero_clienti
            return

        clienti_per_cassa = numero_clienti // len(casse_aperte)
        clienti_extra = numero_clienti % len(casse_aperte)

        for cassa in casse_aperte:
            clienti_da_aggiungere = clienti_per_cassa + (1 if clienti_extra > 0 else 0)
            cassa.clienti_in_coda += clienti_da_aggiungere
            clienti_extra -= 1 if clienti_extra > 0 else 0

        print(f"{numero_clienti} clienti ridistribuiti tra le casse aperte.")

    def serve_cliente_casuale(self):
        casse_con_clienti = [cassa for cassa in self.casse if cassa.aperta and cassa.clienti_in_coda > 0]
        if not casse_con_clienti:
            print("Nessuna cassa aperta con clienti da servire.")
            return False

        cassa_scelta = random.choice(casse_con_clienti)
        if cassa_scelta.avanti_cliente():
            self.coda_clienti -= 1
            print(f"Cliente servito alla {cassa_scelta.nome_cassiere}.")
            return True
        return False

    def visualizza_stato(self):
        print(f"\nClienti totali in coda: {self.coda_clienti}")
        for cassa in self.casse:
            stato = "aperta" if cassa.aperta else "chiusa"
            print(f"{cassa.nome_cassiere} è {stato}. "
                  f"Clienti in coda: {cassa.clienti_in_coda}, "
                  f"Clienti gestiti: {cassa.clienti_gestiti}, "
                  f"Incasso: {cassa.incasso} euro")

    def visualizza_riepilogo(self):
        totale_incassi = sum(cassa.incasso for cassa in self.casse)
        totale_clienti_gestiti = sum(cassa.clienti_gestiti for cassa in self.casse)
        print(f"\nRiepilogo totale:")
        print(f"Totale incassi: {totale_incassi} euro")
        print(f"Totale clienti gestiti: {totale_clienti_gestiti}")
        print(f"Clienti totali in coda: {self.coda_clienti}")

    def aggiungi_clienti(self, numero, indice=None):
        if indice is None:
            self.aggiungi_clienti_prima_disponibile(numero)
        elif 0 <= indice < len(self.casse) and self.casse[indice].aperta:
            self.casse[indice].aggiungi_clienti(numero)
            self.coda_clienti += numero
            self.controlla_apertura()
        else:
            print("Cassa non valida o chiusa. Impossibile aggiungere clienti.")

    def aggiungi_clienti_prima_disponibile(self, numero):
        casse_aperte = [cassa for cassa in self.casse if cassa.aperta]
        if casse_aperte:
            cassa_meno_clienti = min(casse_aperte, key=lambda c: c.clienti_in_coda)
            cassa_meno_clienti.aggiungi_clienti(numero)
            self.coda_clienti += numero
            self.controlla_distribuzione()
            self.controlla_apertura()
        else:
            print("Nessuna cassa aperta. Impossibile aggiungere clienti.")

    def controlla_apertura(self):
        clienti_totali = sum(c.clienti_in_coda for c in self.casse if c.aperta)
        if clienti_totali > 5 and not self.casse[1].aperta:
            print("Richiesta di apertura manuale per la Cassa 2.")
        if clienti_totali > 10 and not self.casse[2].aperta:
            print("Richiesta di apertura manuale per la Cassa 3.")

    def controlla_distribuzione(self):
        casse_aperte = [cassa for cassa in self.casse if cassa.aperta]
        clienti_totali = sum(cassa.clienti_in_coda for cassa in casse_aperte)
        if clienti_totali > 5:
            self.distribuisci_equamente(casse_aperte)

    def distribuisci_equamente(self, casse_aperte):
        clienti_totali = sum(c.clienti_in_coda for c in casse_aperte)
        clienti_per_cassa = clienti_totali // len(casse_aperte)
        clienti_extra = clienti_totali % len(casse_aperte)

        for cassa in casse_aperte:
            cassa.clienti_in_coda = clienti_per_cassa + (1 if clienti_extra > 0 else 0)
            clienti_extra -= 1 if clienti_extra > 0 else 0

        print("Clienti ridistribuiti equamente tra le casse aperte.")

    def sposta_clienti(self, indice_da, indice_a, numero_clienti):
        if 0 <= indice_da < len(self.casse) and 0 <= indice_a < len(self.casse):
            cassa_da, cassa_a = self.casse[indice_da], self.casse[indice_a]
            if cassa_da.clienti_in_coda >= numero_clienti:
                cassa_da.clienti_in_coda -= numero_clienti
                cassa_a.clienti_in_coda += numero_clienti
                print(f"{numero_clienti} clienti spostati dalla cassa '{cassa_da.nome_cassiere}' alla cassa '{cassa_a.nome_cassiere}'.")
            else:
                print("Numero di clienti da spostare superiore ai clienti in coda.")
        else:
            print("Indici cassa non validi.")

