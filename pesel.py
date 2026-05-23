def weryfikuj_pesel(pesel):
    wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    
    suma = 0
    for i in range(10):
        suma += int(pesel[i]) * wagi[i]

    ostatnia_cyfra_sumy = suma % 10
    if ostatnia_cyfra_sumy == 0:
        cyfra_kontrolna = 0
    else:
        cyfra_kontrolna = 10 - ostatnia_cyfra_sumy

    if cyfra_kontrolna == int(pesel[10]):
        return 1
    else:
        return 0


numer_pesel = input("Podaj numer PESEL: ")
wynik = weryfikuj_pesel(numer_pesel)
print(wynik)
