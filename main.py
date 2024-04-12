"""
1. Stworzyć klasę Student , która posiada 2 parametry (name i marks) oraz jedną metodę is_passed, która zwraca wartość
logiczną, pozytywną gdy średnia ocen jest > 50 w przeciwnym przypadku negatywną. Następnie należy stworzyć 2 przykładowe
obiekty klasy, tak aby dla pierwszego obiektu metoda zwracała true , a dla drugiego false .
"""
from Student_ import Student


oceny1 = [50, 60, 70, 80]
stud1 = Student("Janek", oceny1)
print(stud1.is_passed())

oceny2 = [10, 20, 30, 40]
stud2 = Student("Ania", oceny2)
print(stud2.is_passed())


# Zad 2

from Library_ import Library
from Employee_ import Employee
from Book_ import Book
from Order_ import Order


biblioteka1 = Library("Warszawa", "Złota", "00-120", "8.00-20.00", "123 456 789")
biblioteka2 = Library("Ełk", "Krótka", "12-321", "8.00-20.00", "987 655 443")

ksiazka1 = Book(biblioteka1, "12-12-1999", "Jan", "Drabina", "3")
ksiazka2 = Book(biblioteka1, "13-01-1898", "Tom", "Bom", "123")
ksiazka3 = Book(biblioteka2, "01-01-1872", "Kamila", "Kabanoski", "1789")
ksiazka4 = Book(biblioteka2, "02-02-1789", "Krzysztof", "Palmowy", "567")
ksiazka5 = Book(biblioteka2, "03-03-2003", "Barbara", "Ananas", "345")

prac1 = Employee(
    "Jan",
    "Kowalski",
    "14-02-1992",
    "23-08-1970",
    "Gdańsk",
    "Jelitkowa",
    "21-123",
    "213 912 149",
)
prac2 = Employee(
    "Anna",
    "Nowak",
    "27-03-2022",
    "01-02-1999",
    "Poznań",
    "Pyrkowa",
    "33-767",
    "234 675 762",
)
prac3 = Employee(
    "Katarzyna",
    "Klopsik",
    "12-04-1410",
    "12-01-1000",
    "Warszawa",
    "Złota",
    "00-123",
    "987 654 321",
)


zam1 = Order(prac1, stud1, [ksiazka1, ksiazka2, ksiazka3], "12-02-2002")
zam2 = Order(prac2, stud2, [ksiazka4, ksiazka5], "13-03-1992")

# print(biblioteka1)
# print(ksiazka1)

print(zam1)
print(zam2)


# Zad 3
class Property:
    def __init__(self, area, rooms: int, price, adres):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.adres = adres

    def __str__(self):
        return (
            "\n\nArea: "
            + self.area
            + "\nRooms: "
            + self.rooms
            + "\nPrice "
            + self.price
            + "\nAdres: "
            + self.adres
        )


class House(Property):
    def __init__(self, area, rooms: int, price, adres, plot: int):
        super().__init__(area, rooms, price, adres)
        self.plot = plot

    def __str__(self):
        return (
            "\n\nArea: "
            + self.area
            + "\nRooms: "
            + self.rooms
            + "\nPrice "
            + self.price
            + "\nAdres: "
            + self.adres
            + "\nPlot: "
            + self.plot
        )


class Flat(Property):
    def __init__(self, area, rooms: int, price, adres, floor):
        super().__init__(area, rooms, price, adres)
        self.floor = floor

    def __str__(self):
        return (
            "\n\nArea: "
            + self.area
            + "\nRooms: "
            + self.rooms
            + "\nPrice "
            + self.price
            + "\nAdres: "
            + self.adres
            + "\nFloor: "
            + self.floor
        )


dom1 = House("123", "3", "300 000 zl", "ul.Majowa 3", "0")
print(dom1)
mieszkanie1 = Flat("300", "4", "123 456zl", "ul.Fajna 12", "4")
print(mieszkanie1)
