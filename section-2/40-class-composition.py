""" Class composition is for cases when you want to say a thing - in 
this case a book - can reside inside of something else - here bookshelf 
- but not be a part of it ore inherit from it directly. """


class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f'BookShelf with {len(self.books)} books.'


class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Book {self.name}'


book = Book('Hairy Pooper')
book2 = Book('Python 101')
shelf = BookShelf(book, book2)
print(shelf)
