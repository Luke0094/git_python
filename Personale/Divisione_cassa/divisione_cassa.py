import random

class Messaggio:
    FORMATI = {
        "apertura_richiesta": "Richiesta di apertura manuale per la {}.",
        "cassa_stato": "La {} è {}.",
        "coda_generale_aggiunta": "Nessuna cassa aperta. {} clienti aggiunti alla coda generale.",
        "clienti_ridistribuiti": "{} clienti ridistribuiti tra le casse aperte.",
        "cliente_servito": "Cliente servito alla {}. Incasso: {} euro.",
        "clienti_aggiunti": "{} clienti aggiunti alla {}.",
        "clienti_spostati": "{} clienti spostati dalla {} alla {}."
    }

    @staticmethod
    def formatta(azione, contenuto):
        if azione in Messaggio.FORMATI:
            return Messaggio.FORMATI[azione].format(*contenuto.split(','))
        return f"{azione}: {contenuto}"

class Osservatore:
    def aggiorna(self, messaggio):
        pass

class Soggetto:
    def __init__(self):
        self._osservatori = []

    def aggiungi_osservatore(self, osservatore):
        self._osservatori.append(osservatore)

    def rimuovi_osservatore(self, osservatore):
        self._osservatori.remove(osservatore)

    def notifica_osservatori(self, messaggio):
        for osservatore in self._osservatori:
            osservatore.aggiorna(messaggio)

class Cassa(Soggetto):
    def __init__(self, nome, posizione, stato="chiusa"):
        self._osservatori = []
        self.nome = nome
        self.posizione = posizione
        self.stato = stato
        self.clienti_in_coda = 0
        self.incasso = 0
        self.clienti_gestiti = 0

    def apri(self):
        if self.stato == "chiusa":
            self.stato = "aperta"
            self.notifica_osservatori(("cassa_stato", f"{self.nome},ora aperta"))
            return True
        else:
            self.notifica_osservatori(("cassa_stato", f"{self.nome},già aperta"))
            return False

    def chiudi(self):
        if self.stato == "aperta":
            clienti_da_ridistribuire = self.clienti_in_coda
            self.stato = "chiusa"
            self.clienti_in_coda = 0
            self.notifica_osservatori(("cassa_stato", f"{self.nome},ora chiusa"))
            return clienti_da_ridistribuire
        else:
            self.notifica_osservatori(("cassa_stato", f"{self.nome},già chiusa"))
            return 0

    def servi_cliente(self):
        if self.stato == "aperta" and self.clienti_in_coda > 0:
            self.clienti_in_coda -= 1
            incasso_cliente = random.randint(1, 50)
            self.incasso += incasso_cliente
            self.clienti_gestiti += 1
            self.notifica_osservatori(("cliente_servito", f"{self.nome},{incasso_cliente}"))
            return incasso_cliente
        return 0

    def aggiungi_clienti(self, numero):
        self.clienti_in_coda += numero
        self.notifica_osservatori(("clienti_aggiunti", f"{numero},{self.nome}"))

class GestoreCoda(Soggetto):
    def __init__(self):
        self._osservatori = []
        self.coda_generale = 0

    def aggiungi_clienti(self, numero):
        self.coda_generale += numero
        self.notifica_osservatori(("clienti_aggiunti", f"{numero},coda generale"))

    def rimuovi_clienti(self, numero):
        if numero <= self.coda_generale:
            self.coda_generale -= numero
            return numero
        else:
            clienti_rimossi = self.coda_generale
            self.coda_generale = 0
            return clienti_rimossi

class GestoreCasse(Osservatore):
    Soglia_prima_apertura = 5
    Soglia_seconda_apertura = 10

    def __init__(self):
        self.casse = [Cassa(f"Cassa {i + 1}", i + 1) for i in range(3)]
        self.gestore_coda = GestoreCoda()
        for cassa in self.casse:
            cassa.aggiungi_osservatore(self)
        self.gestore_coda.aggiungi_osservatore(self)

    def aggiorna(self, messaggio):
        print(Messaggio.formatta(*messaggio))

    def _clienti_totali(self):
        return sum(cassa.clienti_in_coda for cassa in self.casse)

    def apri_cassa(self, indice):
        if 0 <= indice < len(self.casse):
            if self.casse[indice].apri():
                self.ridistribuisci_clienti()
        else:
            print("Indice cassa non valido.")

    def chiudi_cassa(self, indice):
        if 0 <= indice < len(self.casse):
            clienti_da_ridistribuire = self.casse[indice].chiudi()
            if clienti_da_ridistribuire > 0:
                self.ridistribuisci_clienti(clienti_da_ridistribuire)
        else:
            print("Indice cassa non valido.")

    def controlla_apertura(self):
        clienti_totali = self._clienti_totali()
        casse_chiuse = [cassa for cassa in self.casse if cassa.stato == "chiusa"]
        
        if clienti_totali > self.Soglia_prima_apertura and len(casse_chiuse) >= 1:
            print(Messaggio.formatta("apertura_richiesta", casse_chiuse[0].nome))
        
        if clienti_totali > self.Soglia_seconda_apertura and len(casse_chiuse) >= 2:
            for cassa in casse_chiuse[1:]:
                print(Messaggio.formatta("apertura_richiesta", cassa.nome))

    def ridistribuisci_clienti(self, clienti_extra=0):
        casse_aperte = [cassa for cassa in self.casse if cassa.stato == "aperta"]
        clienti_totali = sum(cassa.clienti_in_coda for cassa in casse_aperte) + self.gestore_coda.coda_generale + clienti_extra
        
        if not casse_aperte:
            if clienti_totali > 5:
                self.gestore_coda.aggiungi_clienti(clienti_totali)
            return

        clienti_per_cassa, resto = divmod(clienti_totali, len(casse_aperte))
        
        for cassa in casse_aperte:
            cassa.clienti_in_coda = clienti_per_cassa + (1 if resto > 0 else 0)
            resto -= 1 if resto > 0 else 0

        self.gestore_coda.coda_generale = 0

        if clienti_totali > 0:
            print(Messaggio.formatta("clienti_ridistribuiti", str(clienti_totali)))

    def aggiungi_clienti(self, numero, indice=None):
        casse_aperte = [cassa for cassa in self.casse if cassa.stato == "aperta"]
        
        if not casse_aperte:
            self.gestore_coda.aggiungi_clienti(numero)
            print(Messaggio.formatta("coda_generale_aggiunta", str(numero)))
        elif indice is not None and 0 <= indice < len(self.casse):
            self.casse[indice].aggiungi_clienti(numero)
        else:
            cassa_scelta = random.choice(casse_aperte)
            cassa_scelta.aggiungi_clienti(numero)

        self.controlla_apertura()

    def sposta_clienti(self, indice_da, indice_a, numero_clienti):
        if 0 <= indice_da < len(self.casse) and 0 <= indice_a < len(self.casse):
            cassa_da, cassa_a = self.casse[indice_da], self.casse[indice_a]
            if cassa_da.clienti_in_coda >= numero_clienti:
                cassa_da.clienti_in_coda -= numero_clienti
                cassa_a.clienti_in_coda += numero_clienti
                print(Messaggio.formatta("clienti_spostati", f"{numero_clienti},{cassa_da.nome},{cassa_a.nome}"))
            else:
                print("Numero di clienti da spostare superiore ai clienti in coda.")
        else:
            print("Indici cassa non validi.")

    def visualizza_stato(self):
        for cassa in self.casse:
            print(f"{cassa.nome} è {cassa.stato}. "
                  f"Clienti in coda: {cassa.clienti_in_coda}, "
                  f"Clienti gestiti: {cassa.clienti_gestiti}, "
                  f"Incasso: {cassa.incasso} euro")

    def visualizza_riepilogo(self):
        totale_incassi = sum(cassa.incasso for cassa in self.casse)
        totale_clienti_gestiti = sum(cassa.clienti_gestiti for cassa in self.casse)
        totale_clienti_in_coda = self._clienti_totali()
        clienti_nella_coda_generale = self.gestore_coda.coda_generale

        print(f"\nRiepilogo totale:")
        print(f"Totale incassi: {totale_incassi} euro")
        print(f"Totale clienti gestiti: {totale_clienti_gestiti}")
        print(f"Clienti totali in coda: {totale_clienti_in_coda}")
        print(f"Clienti nella coda generale: {clienti_nella_coda_generale}")