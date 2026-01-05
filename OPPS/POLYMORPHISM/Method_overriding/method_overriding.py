# child class change the behaviour of the method that its get from the parent class

class Vechile:

    def __init__(self, brand, title):

        self.brand = brand

        self.title = title

    def move(self):

        print(self.title, "is moving")

class Car(Vechile):

    def __init__(self, brand, title):
        super().__init__(brand, title)

class Ship(Vechile):

    def __init__(self, brand, title):
        super().__init__(brand, title)

    def move(self):
        print(self.title, "is saleing") # -->>> child class changing the behaviour of the parent

car_instance = Car("toyoto", "fortuner")
ship_instance = Ship("mintow", "titanic")

car_instance.move()
ship_instance.move()


        
