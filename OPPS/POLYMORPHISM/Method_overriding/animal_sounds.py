class Animal:

    def __init__(self, name):

        self.name = name

    def sound(self):

        print(self.name, "sound")

class Dog(Animal):

    def __init__(self, name):
        super().__init__(name) 

    def sound(self): # Method overriding

        print(self.name, "Boww bow") 

class Cat(Animal):

    def __init__(self, name):
        super().__init__(name) 

    def sound(self): ## Method overriding

        print(self.name, "Meowww")  

cat_instance = Cat("cateee")
dog_instance = Dog("dogee")

cat_instance.sound()
dog_instance.sound()