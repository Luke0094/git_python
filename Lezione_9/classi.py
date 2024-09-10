import random


class Personaggio:
    def __init__(self,pf,nome,des,str,int):
        self.pf = pf
        self.nome = nome
        self.des = des
        self.str = str
        self.int = int


    def set_nome(self, nuovo_nome)
        self.nome = nuovo_nome

    def attacca(self):
        return random.randint(0,6)
    

class Ladro(Personaggio):
        def nasconditi(self):
            print("Mi sono nascosto!")

        def scassina(self):
            print("Ho scassinato la serratura!")



class Mago(Personaggio):
     def attacco_speciale


class Guerriero(Personaggio):