class Library:
    def __init__(self, city, street, zip_code, open_hours: str, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (
            "\n\nmiasto: "
            + self.city
            + "\nulica: "
            + self.street
            + "\nkod pocztowy: "
            + self.zip_code
            + "\ngodzinny otwarcia: "
            + self.open_hours
            + "\ntelefon: "
            + self.phone
        )