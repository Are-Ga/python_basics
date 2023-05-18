# simple reminder to self on how to use classes
# extremely heavily inspired by freeCodeCamp Harvard CS50’s Introduction to Programming with Python
# taught by Dr. David J. Malan.

# the classes will make a unique dataset of values for the current needs
class Student:
    def __init__(self, name, house, patronus):
        # more pythonic than to if name == ""
        if not name:
            # can raise error and specify a helping comment
            raise ValueError("Missing name")
        if not house in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house
        self.patronus = patronus

    # printing a class will result in printing the object itself, and the menory location.
    # we can control what to print with the __str__ function.
    def __str__(self):
        return f"{self.name} from {self.house}"

    # we can make our own function within the class
    def charm(self):
        match self.patronus:
            case "Stag":
                return "x"
            case "Otter":
                return "y"
            case "Jack Russel terrier":
                return "z"
            case _:
                return "-"

def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())


def get_student():
    name = input("Name? ")
    house = input("House? ")
    patronus = input("Patronus? ")
    return Student(name, house, patronus)

# make sure to run program only when called directly, not when imported
if __name__ == "__main__":
    main()
