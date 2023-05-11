# Super Class.
class Car:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def material_used(self):
        pass

    def all_cars(self):
        return f"name = {self.name}, type = {self.type}\n"



# Sub Class, ingerited from Car class.
class Electirc_car(Car):
    def __init__(self, name, type):
        super().__init__(name, type)
    
    def material_used(self):
        return "elecric_charge"


# Another Sub Class, ingerited from Car class.
class Petrol_car(Car):
    def __init__(self, name, type):
        super().__init__(name, type)

    def material_used(self):
        return "petrol"


# Objects of "Electric_car" class and "Petrol_car".
electric_car1 = Electirc_car("Tesla", "Electric")
petrol_car1 = Petrol_car("Alto 800", "Patrol Car")


print(electric_car1.all_cars())
print(petrol_car1.all_cars())


