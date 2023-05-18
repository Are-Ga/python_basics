# sets

students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"}
]

# manual approach to find unique values
houses = []
for student in students:
    if student["house"] not in houses:
        houses.append(student["house"])

for house in sorted(houses):
    print(house)

# unique values can also be easily found with the set() function in python
houses_new = set()
for student in students:
    houses_new.add(student["house"])

print(houses_new)

for house in sorted(houses_new):
    print(house)