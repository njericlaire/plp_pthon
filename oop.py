


class Vehicle:
    def __init__(self,color,model,date_of_make):
        self.color=color
        self.model=model 
        self.date_of_make=date_of_make

class Car(Vehicle):
    def __init__(self, color, model, date_of_make,number_of_tyres):
        super().__init__(color, model, date_of_make)
        self.number_of_tyres=number_of_tyres


# Activity 2: Polymorphism Challenge! 🎭

class Car:
    def __init__(self) -> None:
        pass
    def move(self):
        print("Driving")


class Plane:
    def __init__(self) -> None:
        pass
    def move(self):
        print("Flying")

class Bike:
    def __init__(self) -> None:
        pass
    def move(self):
        print("Riding")
