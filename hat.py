import random

class Hat:
    # we dont need to init when we want a class-method as the variable houses will be available for all instnances.
    # def __init__(self):

    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in",  random.choice(cls.houses))

# no need to create a instance of the class, we can just directly call it.
#hat = Hat()
Hat.sort("Harry")
