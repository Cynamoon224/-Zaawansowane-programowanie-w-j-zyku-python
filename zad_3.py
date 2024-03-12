def parzyste(liczby):
    for i in range(len(liczby)):
        if liczby[i] % 2 == 0:
            print(liczby[i])


numerki10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

parzyste(numerki10)
