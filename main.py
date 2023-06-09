# simple reminder to self on how to use classes
# extremely heavily inspired by freeCodeCamp Harvard CS50’s Introduction to Programming with Python
# taught by Dr. David J. Malan.

# the classes will make a unique dataset of values for the current needs
class Student:
    def __init__(self, name, house):
        self.name = name
        # notice that if we make this self._house it will circumvent the error-checker below
        self.house = house
    # printing a class will result in printing the object itself, and the memory location.
    # we can control what to print with the __str__ function.
    def __str__(self):
        return f"{self._name} from {self._house}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        # more pythonic than to if name == ""
        if not name:
            # can raise error and specify a helping comment
            raise ValueError("Missing name")
        self._name = name

    # getter
    @property
    def house(self):
        return self._house()

    # setter
    @house.setter
    def house(self, house):
        if not house in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self._house = house

    # introduced a classmethod to replace the get_student() function from before
    # this in order to collect all the relevant code that applies to the Students class
    @classmethod
    def get(cls):
        name = input("Name? ")
        house = input("House? ")
        return cls(name, house)



def main():
    student = Student.get()
    print(student)

# make sure to run program only when called directly, not when imported
if __name__ == "__main__":
    main()
