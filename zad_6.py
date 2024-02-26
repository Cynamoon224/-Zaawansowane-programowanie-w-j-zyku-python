# Zad 6


def listy(l1: list, l2: list) -> list:
    wynik = list(set(l1+l2))
    return wynik


l1 = [1, 2, 3, 4, 5, 6]
l2 = [3, 4, 5, 6, 7, 8, 9]

print(listy(l1, l2))