class Car:

    name :str

    brand : str

    price : int

    color : str


    def set_car(self, name, brand, price, color):

        self.name = name
        self.brand = brand
        self.price = price
        self.color = color

    def display(self):

        print(f"Car name : {self.name}")
        print(f"Car brand : {self.brand}")
        print(f"Car price : {self.price}")
        print(f"Car color : {self.color}")


car_instance_01 = Car() # create a object

car_instance_01.set_car("Thar", "Mahindra", 1800000, "black")

car_instance_01.display()

