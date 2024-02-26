# Zad 5

def czy_zawiera(lista: list, x: int) -> bool:

    if x in lista:
        return True
    else:
        False


liczby = [1, 2, 3, 4]
print(czy_zawiera(liczby, 2))