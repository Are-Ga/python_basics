# inheritance
# why name class Student and class Professor if they are both Wizards and have features in common?
# we were to duplicate error checking for the separate classes and duplicate code is always to be avoided.

class Wizard:
    def __init__(self,name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

        ...


class Student(Wizard):
    def __init__(self, name, house):
        # will call the __init__ from the super-class or parent-class
        super().__init__(name)
        self.name = name
        self.house = house

        ...


class Professor(Wizard):
    def __int__(self, name, subject):
        super().__int__(name)
        self.name = name
        self subject = subject

        ...


wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defence Against the Dark Arts")
