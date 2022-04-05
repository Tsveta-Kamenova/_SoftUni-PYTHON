class Dog:
    def __init__(self, name, age, legs):
        self.name = name
        self.age = age
        self.legs = legs

    def produce_sound(self):
        sound = "I'm a Distinguishedog, and I will now produce a distinguished sound! Bau Bau."
        return sound


class Cat:
    def __init__(self, name, age, iq):
        self.name = name
        self.age = age
        self.iq = iq

    def produce_sound(self):
        sound = "I'm an Aristocat, and I will now produce an aristocratic sound! Myau Myau."
        return sound


class Snake:
    def __init__(self, name, age, cruelty):
        self.name = name
        self.age = age
        self.cruelty = cruelty

    def produce_sound(self):
        sound = "I'm a Sophistisnake, and I will now produce a sophisticated sound! Honey, I'm home."
        return sound


list_animals = []
list_talks = []

data_input = input()

while data_input != "I'm your Huckleberry":

    data_input = data_input.split()
    class_animal = data_input[0]

    if class_animal != "talk":

        current_animal_name = data_input[1]
        current_animal_age = int(data_input[2])
        current_animal_param = int(data_input[3])

        if class_animal == "Dog":
            current_animal = Dog(current_animal_name, current_animal_age, current_animal_param)
        elif class_animal == "Cat":
            current_animal = Cat(current_animal_name, current_animal_age, current_animal_param)
        elif class_animal == "Snake":
            current_animal = Snake(current_animal_name, current_animal_age, current_animal_param)

        list_animals.append(current_animal)

    else:
        current_name_talk = data_input[1]
        for item in list_animals:
            if current_name_talk == item.name:
                list_talks.append(item)

    data_input = input()

for item in list_talks:
    print(item.produce_sound())

num = 0
n = len(list_animals)

for num in range(0, n-1):
    for i in range(n-1, 0, -1):
        if isinstance(list_animals[i], Dog) and not isinstance(list_animals[i-1], Dog):
            list_animals[i], list_animals[i-1] = list_animals[i-1], list_animals[i]

for item in list_animals:
    if isinstance(item, Dog):
        print(f"Dog: {item.name}", end=", ")
        print(f"Age: {item.age}", end=", ")
        print(f"Number Of Legs: {item.legs}")
    if isinstance(item, Cat):
        print(f"Cat: {item.name}", end=", ")
        print(f"Age: {item.age}", end=", ")
        print(f"IQ: {item.iq}")
    if isinstance(item, Snake):
        print(f"Snake: {item.name}", end=", ")
        print(f"Age: {item.age}", end=", ")
        print(f"Cruelty: {item.cruelty}")
