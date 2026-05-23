import re
import sys


def czysc_tekst(tekst):
    tekst = tekst.lower()
    tekst = re.sub(r'[^a-z0-9\s]', ' ', tekst)
    return tekst.split()


def stworz_indeks(dane_wejsciowe):
    wejscie = iter(dane_wejsciowe)
    try:
        n = int(next(wejscie))
        dokumenty = []

        for _ in range(n):
            dokumenty.append(czysc_tekst(next(wejscie)))

        m = int(next(wejscie))
        zapytania = []
        for _ in range(m):
            zapytania.append(next(wejscie).strip().lower())

        for zapytanie in zapytania:
            wyniki_dokumentow = []

            for idx, doc in enumerate(dokumenty):
                czestosc = doc.count(zapytanie)
                if czestosc > 0:
                    wyniki_dokumentow.append((idx, czestosc))

            wyniki_dokumentow.sort(key=lambda x: (-x[1], x[0]))

            koncowa_lista = [para[0] for para in wyniki_dokumentow]
            print(koncowa_lista)

    except StopIteration:
        pass



if __name__ == "__main__":
    przykladowe_dane = [
        "3",
        "Your care set up, do not pluck my care down.",
        "My care is loss of care with old care done.",
        "Your care is gain of care when new care is won.",
        "2",
        "care",
        "is"
    ]
    stworz_indeks(przykladowe_dane)