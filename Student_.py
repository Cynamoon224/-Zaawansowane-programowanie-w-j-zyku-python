class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        suma = 0
        for i in self.marks:
            suma += i
        if suma / len(self.marks) > 50:
            return True
        else:
            return False

    def __str__(self):
        return "\n\nImię: " + self.name + "\noceny: " + str(self.marks)