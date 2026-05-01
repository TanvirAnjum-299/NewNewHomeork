#Define a class(blueprint)
class Car:
    def __init__(self,brand,model):
        self.brand=brand #Attribute
        self.model=model #Attribute
    def drive(self):
        print(f"{self.brand}{self.model} is driving")
#Create objects(instances of Car)
car1 = Car("Toyota", "Corolla")
car2 = Car("Tesla", "Model S")
car3 = Car("BMW", "X5")

# Use objects
car1.drive()
car2.drive()
car3.drive()
