import csv
from datetime import datetime

def dodaj_zadanie(nazwa_pliku):
    with open(nazwa_pliku, mode='a', newline='') as plik:
        pisarz = csv.writer(plik)
        obecny_czas = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        pisarz.writerow([obecny_czas, 'pending'])

if __name__ == '__main__':
    dodaj_zadanie('zadania.csv')
