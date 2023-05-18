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
        # notice, we need to use a new variable name in order to avoid conflict.
        # the convention is to use underscore to indicate that is "almost" the same
        return self._house()

    # setter
    @house.setter
    # function that will be accessed instead of the atribute house itself when calling student.house
    # highly useful error checking and avoiding circumventing the checker at initiation of the class
    # this will be called when initializing the class.
    def house(self, house):
        if not house in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self._house = house


def main():
    student = get_student()
    # following line will break the program due to the validation:
    # student.house = "Number Four, Privet Drive"

    # on closing remarks, we are still able to change the student._house variable
    # however the convention is to never touch variables starting with underscore.

    print(student)


def get_student():
    name = input("Name? ")
    house = input("House? ")
    return Student(name, house)

# make sure to run program only when called directly, not when imported
if __name__ == "__main__":
    main()
