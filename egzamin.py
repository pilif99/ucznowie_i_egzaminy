class Egzamin:

    def __init__(self, nazwa):

        self.nazwa = nazwa
        self.lista_ocen = []

    def get_nazwa(self):
        
        return self.nazwa

    def get_lista_ocen(self):
        
        return self.lista_ocen 

    def dodaj_ocene(self, ocena):

        self.lista_ocen.append(int(ocena))

    def wyswietl_oceny(self):
        print(self.lista_ocen)

    def oblicz_srednia(self):
        return sum(self.lista_ocen)/len(self.lista_ocen)
