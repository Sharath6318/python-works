class Person:

    def __init__(self, name, age, gender):

        self.name = name

        self.age = age

        self.gender = gender

    # def get_name(self): Normal Way.............

    #     print(self.name)

    @property # decorator property..............................................

    def get_name(self):

        print(self.name)



new_person_instance = Person("sharath", 21, "male")

# new_person_instance.get_name()  # Noraml way to call Method..................

new_person_instance.get_name #......................... call method use decorator we dont want to use ()
        