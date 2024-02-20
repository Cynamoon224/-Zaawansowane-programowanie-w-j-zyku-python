def liczby(lista):
    for i in range(len(lista)):
        lista[i] = lista[i]*2
    return lista


numerki = [1, 2, 3, 4, 5]
print(liczby(numerki))

numerki = [1, 2, 3, 4, 5]
numerki_2 = [number*2 for number in numerki]
print(numerki_2)