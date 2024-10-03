import random

class Cassa:
    def __init__(self, nome_cassiere, posizione, aperta=False):
        self.nome_cassiere = nome_cassiere
        self.posizione = posizione
        self.aperta = aperta
        self.clienti_serviti = 0
        self.incasso = 0  # Inizializza l'incasso

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
            # Genera un incasso casuale tra 5 e 20 euro
            incasso_cliente = random.randint(5, 20)
            self.incasso += incasso_cliente
            print(f"Un cliente è stato servito alla cassa '{self.nome_cassiere}'. Clienti serviti: {self.clienti_serviti}. Incasso: {incasso_cliente} euro.")
        else:
            print(f"La cassa '{self.nome_cassiere}' è chiusa. Impossibile servire clienti.")

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
            cassa_aperta = [cassa for cassa in self.casse if cassa.aperta]
            if cassa_aperta:
                cassa_migliore = min(cassa_aperta, key=lambda cassa: cassa.clienti_serviti)
                
                # Numero casuale di clienti da servire (fino a 3)
                clienti_da_servire = random.randint(1, min(3, self.coda_clienti))
                print(f"Servire {clienti_da_servire} clienti dalla cassa '{cassa_migliore.nome_cassiere}'.")

                # Servire i clienti uno per volta
                for _ in range(clienti_da_servire):
                    self.coda_clienti -= 1
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