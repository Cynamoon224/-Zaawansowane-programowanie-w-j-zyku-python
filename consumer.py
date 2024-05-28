import csv
import time
from datetime import datetime

def przetwarzaj_zadanie(nazwa_pliku):
    while True:
        time.sleep(5)
        zadania = []
        with open(nazwa_pliku, mode='r', newline='') as plik:
            czytelnik = csv.reader(plik)
            for wiersz in czytelnik:
                if wiersz[1] == 'pending':
                    wiersz[1] = 'in_progress'
                    time.sleep(30)
                    wiersz[1] = 'done'
                zadania.append(wiersz)
        
        with open(nazwa_pliku, mode='w', newline='') as plik:
            pisarz = csv.writer(plik)
            pisarz.writerows(zadania)

if __name__ == '__main__':
    przetwarzaj_zadanie('zadania.csv')
