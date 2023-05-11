class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        pass

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed
        
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, species="Cat")
        self.color = color
        
    def make_sound(self):
        return "Meow!"
    
class Shelter:
    def __init__(self):
        self.animals = []
        
    def add_animal(self, animal):
        self.animals.append(animal)
        
    def show_animals(self):
        for animal in self.animals:
            print(f"{animal.name} ({animal.species})")

dog1 = Dog("Fido", "Labrador")
cat1 = Cat("Whiskers", "Calico")
shelter1 = Shelter()
shelter1.add_animal(dog1)
shelter1.add_animal(cat1)
shelter1.show_animals()
