import argparse


def weryfikuj_nawiasy(tekst):
    licznik = 0

    for znak in tekst:
        if znak == '(':
            licznik += 1
        elif znak == ')':
            licznik -= 1

        if licznik < 0:
            return False

    if licznik == 0:
        return True
    else:
        return False


# URUCHAMIANIE PROGRAMU
if __name__ == "__main__":

    tekst_testowy = "I told (that its not (yet) done). (42)"

    try:
        parser = argparse.ArgumentParser(description="Weryfikacja nawiasów")
        parser.add_argument("identifier", type=str, nargs='?', default=tekst_testowy)
        args = parser.parse_args()
        wynik = weryfikuj_nawiasy(args.identifier)
        print(wynik)
    except:
        wynik = weryfikuj_nawiasy(tekst_testowy)
        print(wynik)