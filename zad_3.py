# Zad 3


def parzyste(liczba) -> bool:
    if liczba % 2 == 0:
        return True
    else:
        return False


wynik = parzyste(3)
if wynik is True:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")