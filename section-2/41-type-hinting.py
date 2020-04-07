from typing import List


def list_avg(sequence: List) -> float:
    """ Here we see type hinting. "sequence" is expecting a list
    and the method as a whole returns a float value denoted by 
    "-> float" """
    return sum(sequence) / len(sequence)


list_avg(123)


class Book:
    TYPES = ('hardcover', 'paperback')

    def __init__(self, name: str, book_type: str, weight: int):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self) -> str:
        return f'<Book(name={self.name}, book_type={self.book_type}, weight={self.weight})>'

    @classmethod
    def hardcover(cls, name: str, page_weight: int) -> "Book":
        """ Note that for class methods if you refer to the class as the
        return type it must be in quotes as class methods are 
        initialized at the same time as the class. """
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.TYPES[1], page_weight)


class BookShelf:
    def __init__(self, books: List[Book]):
        self.books = books

    def __str__(self) -> str:
        return f'BookShelf with {len(self.books)} books.'
