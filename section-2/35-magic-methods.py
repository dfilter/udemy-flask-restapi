class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        """ this method is called when you want to return a class 
        instance as a string """
        return f'Person {self.name}, is {self.age} years old.'

    def __repr__(self):
        """ this method is supposed to be an unambiguous method that 
        makes it easy to recreate an object.  """
        return f'<Person(name={self.name}, age={self.age})>'


bob = Person('Bob', 35)
print(bob)
