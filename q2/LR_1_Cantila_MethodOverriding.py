class Animal:
    def __init__(self, name):
        self.__name = name

    def make_sound(self):
        print(f"{self.__name} makes a sound.")

    def eat(self):
            print(f"{self.__name} is eating.")

class Lion(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.__name = "Simba"

    def make_sound(self):
        print(f"{self.__name} roars loudly!")

    def eat(self):
        print(f"{self.__name} eats fresh meat.")

class Elephant(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.__name = "Dumbo"

    def make_sound(self):
        print(f"{self.__name} trumpets!")

    def eat(self):
        print(f"{self.__name} eats grass and fruits.")

class Monkey(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.__name = "George"

    def make_sound(self):
        print(f"{self.__name} chatters!")

    def eat(self):
        print(f"{self.__name} eats bananas.")

Lion("Simba").make_sound()
Lion("Simba").eat()
print("-----")

Elephant("Dumbo").make_sound()
Elephant("Dumbo").eat()
print("-----")

Monkey("George").make_sound()
Monkey("George").eat()
print("-----")


