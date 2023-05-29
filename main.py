from uczen import Uczen
from egzamin import Egzamin

lista_uczniow = []
slownik_egzaminow = {}

liczba_uczniow = int(input('Wpisz liczbę uczniów: '))

for i in range(liczba_uczniow):
    x = input('Podaj oceny ucznia: ').split(' ')
    lista_uczniow.append(Uczen(x[0]))
    for i in range(len(x)-1):
        egzamin = x[i+1].split(':')[0]
        ocena = x[i+1].split(':')[1]
        if not egzamin in slownik_egzaminow.keys():
            slownik_egzaminow[egzamin] = Egzamin(egzamin)
        slownik_egzaminow[egzamin].dodaj_ocene(ocena)
        lista_uczniow[-1].dodaj_ocene(egzamin, ocena)
            
for i in range(len(lista_uczniow)):

    print(lista_uczniow[i].get_imie())
    print(lista_uczniow[i].oblicz_srednia())

for i in slownik_egzaminow.keys():

    print(i)
    print(slownik_egzaminow[i].oblicz_srednia())
