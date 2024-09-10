from classi import attacco_speciale
class combattimento:
    def __init__(self, pg, mostro):
        self.pg = pg
        self.mostro = mostro

        def start(self):
            danni = self,pg.attacca()
            self.mostro.ferisci(danni)
    
    def combat(self):
        danni = self.pg.attacca()
        self.mostro.ferisci(danni)

        def combat_speciale(self):
            danni = self.pg.attacco_speciale
            self.mostro.ferisci(danni)