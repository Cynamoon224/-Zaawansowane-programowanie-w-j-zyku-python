from Library_ import Library

class Book:
    def __init__(
        self,
        library: Library,
        publication_date,
        author_name,
        author_surname,
        number_of_pages,
    ):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (
            self.library.__str__()
            + "\n\ndata publikacji: "
            + self.publication_date
            + "\nimie autora: "
            + self.author_name
            + "\nnazwisko autora: "
            + self.author_surname
            + "\nliczba stron: "
            + self.number_of_pages
        )

