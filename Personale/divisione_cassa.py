import random

class Cassa:
    def __init__(self, nome_cassiere, posizione, aperta=False):
        self.nome_cassiere = nome_cassiere
        self.posizione = posizione
        self.aperta = aperta
        self.clienti_in_coda = 0
        self.incasso = 0

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
        self.casse = [
            Cassa("Cassa 1", 1),
            Cassa("Cassa 2", 2),
            Cassa("Cassa 3", 3)
        ]
        self.coda_clienti = 0
        self.avviso_casse_chiuse_inviato = False  # Inizialmente non inviato

    def apri_cassa(self, indice):
        if 0 <= indice < len(self.casse):
            cassa = self.casse[indice]
            cassa.apri()
            self.controlla_distribuzione()
            self.avviso_casse_chiuse_inviato = False  # Resetta l'avviso quando una cassa è aperta
        else:
            print("Indice cassa non valido.")

    def chiudi_cassa(self, indice):
        if 0 <= indice < len(self.casse):
            cassa = self.casse[indice]
            if cassa.aperta:
                clienti_da_ridistribuire = cassa.clienti_in_coda
                print(f"Chiudendo la cassa '{cassa.nome_cassiere}'. Clienti da ridistribuire: {clienti_da_ridistribuire}.")
                cassa.chiudi()
                cassa.clienti_in_coda = 0
                self.ridistribuisci_clienti_equamente(clienti_da_ridistribuire)
            else:
                print(f"La cassa '{cassa.nome_cassiere}' è già chiusa.")
        else:
            print("Indice cassa non valido.")

    def serve_cliente(self):
        casse_aperte = [cassa for cassa in self.casse if cassa.aperta]
        casse_chiuse = [cassa for cassa in self.casse if not cassa.aperta]

        if not casse_aperte:
            print("Nessuna cassa aperta. Impossibile servire clienti.")
            return False

        if casse_chiuse and not self.avviso_casse_chiuse_inviato:
            print("Attenzione: ci sono casse chiuse con clienti in coda. Questi clienti non possono essere serviti.")
            self.avviso_casse_chiuse_inviato = True

        cassa_con_piu_clienti = max(casse_aperte, key=lambda c: c.clienti_in_coda)
        if cassa_con_piu_clienti.avanti_cliente():
            self.coda_clienti -= 1
            return True

        return False

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
        if not casse_aperte:
            print("Nessuna cassa aperta. Impossibile aggiungere clienti.")
            return

        cassa_meno_clienti = min(casse_aperte, key=lambda c: c.clienti_in_coda)
        cassa_meno_clienti.aggiungi_clienti(numero)
        self.coda_clienti += numero
        self.controlla_distribuzione()
        self.controlla_apertura()

    def sposta_clienti(self, indice_da, indice_a, numero_clienti):
        if 0 <= indice_da < len(self.casse) and 0 <= indice_a < len(self.casse):
            cassa_da = self.casse[indice_da]
            cassa_a = self.casse[indice_a]
            if cassa_da.clienti_in_coda >= numero_clienti:
                cassa_da.clienti_in_coda -= numero_clienti
                cassa_a.clienti_in_coda += numero_clienti
                print(f"{numero_clienti} clienti spostati dalla cassa '{cassa_da.nome_cassiere}' alla cassa '{cassa_a.nome_cassiere}'.")
            else:
                print("Numero di clienti da spostare superiore ai clienti in coda.")
        else:
            print("Indici cassa non validi.")

    def controlla_distribuzione(self):
        casse_aperte = [cassa for cassa in self.casse if cassa.aperta]
        clienti_totali = sum(cassa.clienti_in_coda for cassa in casse_aperte)

        if clienti_totali > 5:
            self.distribuisci_equamente(casse_aperte)
        else:
            for cassa in casse_aperte:
                if cassa.clienti_in_coda > 5:
                    clienti_da_spostare = cassa.clienti_in_coda - 5
                    cassa.clienti_in_coda = 5
                    self.ridistribuisci_clienti(clienti_da_spostare)

    def distribuisci_equamente(self, casse_aperte):
        clienti_totali = sum(cassa.clienti_in_coda for cassa in casse_aperte)
        clienti_per_cassa = clienti_totali // len(casse_aperte)
        clienti_extra = clienti_totali % len(casse_aperte)

        for cassa in casse_aperte:
            cassa.clienti_in_coda = clienti_per_cassa
            if clienti_extra > 0:
                cassa.clienti_in_coda += 1
                clienti_extra -= 1

        print("Clienti ridistribuiti equamente tra le casse aperte.")

    def ridistribuisci_clienti(self, numero_clienti):
        casse_disponibili = [cassa for cassa in self.casse if cassa.aperta and cassa.clienti_in_coda < 5]

        while numero_clienti > 0:
            if not casse_disponibili:
                break
            
            for cassa in casse_disponibili:
                if numero_clienti > 0:
                    cassa.clienti_in_coda += 1
                    numero_clienti -= 1

            casse_disponibili = [cassa for cassa in self.casse if cassa.aperta and cassa.clienti_in_coda < 5]

    def ridistribuisci_clienti_equamente(self, numero_clienti):
        casse_aperte = [cassa for cassa in self.casse if cassa.aperta]
        if not casse_aperte:
            print("Nessuna cassa aperta. Impossibile redistribuire clienti.")
            return
        
        clienti_totali = sum(cassa.clienti_in_coda for cassa in casse_aperte) + numero_clienti
        clienti_per_cassa = clienti_totali // len(casse_aperte)
        clienti_extra = clienti_totali % len(casse_aperte)

        for cassa in casse_aperte:
            cassa.clienti_in_coda = clienti_per_cassa
            if clienti_extra > 0:
                cassa.clienti_in_coda += 1
                clienti_extra -= 1

        print(f"Clienti redistribuiti equamente dopo la chiusura. Clienti totali: {clienti_totali}.")

    def controlla_apertura(self):
        clienti_totali = sum(cassa.clienti_in_coda for cassa in self.casse)
        if clienti_totali > 5 and not self.casse[1].aperta:
            print("Richiesta di apertura manuale per la Cassa 2.")
        if clienti_totali > 10 and not self.casse[2].aperta:
            print("Richiesta di apertura manuale per la Cassa 3.")

    def visualizza_stato(self):
        for cassa in self.casse:
            stato = "aperta" if cassa.aperta else "chiusa"
            print(f"{cassa.nome_cassiere} è {stato}. Clienti in coda: {cassa.clienti_in_coda}.")
        print(f"Clienti totali in coda: {self.coda_clienti}.")

    def visualizza_incassi(self):
        for cassa in self.casse:
            cassa.visualizza_incasso()



       





"""
class Cassa:
    def __init__(self, nome_cassiere, posizione, aperta=False):
        self.nome_cassiere = nome_cassiere
        self.posizione = posizione
        self.aperta = aperta
        self.clienti_serviti = 0

    def apri(self):
        if not self.aperta:
            self.aperta = True
            print(f"La cassa '{self.nome_cassiere}' è ora aperta.")

    def chiudi(self):
        if self.aperta:
            self.aperta = False
            print(f"La cassa '{self.nome_cassiere}' è ora chiusa.")

    def avanti_cliente(self):
        if self.aperta:
            self.clienti_serviti += 1
            print(f"Un cliente è stato servito alla cassa '{self.nome_cassiere}'. Clienti serviti: {self.clienti_serviti}.")
        else:
            print(f"La cassa '{self.nome_cassiere}' è chiusa. Impossibile servire clienti.")

class GestoreCasse:
    def __init__(self):
        self.casse = [
            Cassa("Cassa 1", 1),
            Cassa("Cassa 2", 2),
            Cassa("Cassa 3", 3)
        ]
        self.coda_clienti = 0

    def apri_cassa(self, indice):
        if 0 <= indice < len(self.casse):
            self.casse[indice].apri()
        else:
            print("Indice cassa non valido.")

    def chiudi_cassa(self, indice):
        if 0 <= indice < len(self.casse):
            self.casse[indice].chiudi()
        else:
            print("Indice cassa non valido.")

    def serve_cliente(self):
        if self.coda_clienti > 0:
            self.coda_clienti -= 1
            cassa_aperta = [cassa for cassa in self.casse if cassa.aperta]
            if cassa_aperta:
                cassa_migliore = min(cassa_aperta, key=lambda cassa: cassa.clienti_serviti)
                cassa_migliore.avanti_cliente()
            else:
                print("Nessuna cassa è aperta.")
        else:
            print("Nessun cliente in coda.")

    def aggiungi_clienti(self, numero):
        if self.casse[0].aperta:  # Verifica se la Cassa 1 è aperta
            self.coda_clienti += numero
            print(f"{numero} clienti aggiunti alla coda. Clienti in coda: {self.coda_clienti}.")
            self.controlla_apertura()
        else:
            print("Devi aprire la Cassa 1 prima di aggiungere clienti.")

    def controlla_apertura(self):
        if self.coda_clienti > 5 and not self.casse[1].aperta:  # Cassa 2
            self.apri_cassa(1)
        if self.coda_clienti > 10 and not self.casse[2].aperta:  # Cassa 3
            self.apri_cassa(2)

    def visualizza_stato(self):
        for cassa in self.casse:
            stato = "aperta" if cassa.aperta else "chiusa"
            print(f"{cassa.nome_cassiere} è {stato}. Clienti serviti: {cassa.clienti_serviti}.")
        print(f"Clienti in coda: {self.coda_clienti}.")
"""