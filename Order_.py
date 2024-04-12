from Employee_ import Employee
from Student_ import Student
from Book_ import Book


class Order:
    def __init__(self, employee: Employee, student: Student, books: Book, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        ksiazki = ""
        for i in self.books:
            ksiazki += str(i)
        return (
            "\n"
            + self.employee.__str__()
            + "\nStudent: "
            + self.student.__str__()
            + "\nKsiążki: "
            + ksiazki
            + "\nData zamowienia: "
            + self.order_date
        )