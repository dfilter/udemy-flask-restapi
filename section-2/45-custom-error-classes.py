class TooManyPagesReadError(ValueError):
    pass

class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0

    def __repr__(self):
        return f'<Book(name={self.name}, page_count={self.page_count})>'

    def read(self, pages: int):
        if self.pages_read + pages > self.page_count:
            raise TooManyPagesReadError(
                f'You tried to read {self.pages_read + pages} pages but {self.name} only has {self.page_count} pages.'
            )
        self.pages_read += pages
        print(f'You have now read {self.pages_read} out of {self.page_count}')

try:
    book = Book('Python101', 50)
    book.read(35)
    book.read(50)
except TooManyPagesReadError as e:
    print(e)
