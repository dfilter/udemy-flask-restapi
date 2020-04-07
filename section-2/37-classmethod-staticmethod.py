class ClassTest:
    def instance_method(self):
        """ instance methods automatically receives this instance of the 
        class when they are called. """
        print(f'Called instance method of {self}')

    @classmethod
    def class_method(cls):
        """ class method automatically receives entire class when 
        called. """
        print(f'Called class_method of {cls}')

    @staticmethod
    def static_method():
        """ static methods receive no arguments by default when called. 
        Note that such methods do not have access to the class or class
        instance. """
        print('Called static_method')


class Book:
    TYPES = ('hardcover', 'paperback')

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f'<Book(name={self.name}, book_type={self.book_type}, weight={self.weight})>'

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)


book = Book.paperback('Hairy Pooper', 1500)
print(book)
