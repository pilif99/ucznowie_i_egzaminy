class Uczen:

    def __init__(self, imie):

        self.imie = imie
        self.slownik_ocen = {}

    def get_imie(self):

        return self.imie
    
    def get_slownik_ocen(self):

        return self.slownik_ocen

    def dodaj_ocene(self, nazwa, ocena):
        if nazwa in list(self.slownik_ocen.keys()):
            self.slownik_ocen[nazwa].append(ocena)
        else:
            self.slownik_ocen[nazwa] = [ocena]

    def wyswietl_oceny(self):
        print(self.slownik_ocen)

    def oblicz_srednia(self):
        lista = []
        for i in self.slownik_ocen.values():
            lista.extend(i)
        for i in range(len(lista)):
            lista[i] = int(lista[i])
        return sum(lista)/len(lista)
