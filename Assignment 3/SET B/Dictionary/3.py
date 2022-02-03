#3. Write a Python program to get a dictionary from an object's fields.

class Student:
    def __init__(self, roll, name, _class):
        self.roll = roll
        self.name = name
        self._class = _class

object = Student("1", "Shubham", "MSc CS - I")

student_dict = object.__dict__.copy()

print("\nDictionary from student object: ", student_dict)