from typing import List, Optional

class Student:
    def __init__(self, name: str, grades: Optional[List[int]] = []):
        """ It is never good to assign a mutable type as a default 
        parameter. This is bad because the default value is assigned
        when the function is defined, not when it is called. Therefor 
        for both bob and rolf below they wil have the same list of 
        grades because both are pointing to the same list. It is ok
        to assign default values if the value type is tuple, str, float,
        int, or bool. """
        self.name = name
        self.grades = grades

    def take_exam(self, result: int):
        self.grades.append(result)



class Student:
    def __init__(self, name: str, grades: Optional[List[int]] = None):
        """ This is the correct way to define a mutable default 
        parameter. """
        self.name = name
        self.grades = grades or []

    def take_exam(self, result: int):
        self.grades.append(result)


bob = Student('Bob')
rolf = Student('Rolf')
bob.take_exam(90)
print(bob.grades)
print(rolf.grades)
