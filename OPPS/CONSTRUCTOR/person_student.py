class person:

    name : int

    age:int

    gender:int

    def __init__(self, name, age, gender):

        self.name = name

        self.age = age

        self.gender = gender

    def display(self):

        print(f"Name : {self.name} Age : {self.age} gender : {self.gender}")


class student(person):

    rol_num : int

    course : str

    def __init__(self, name, age, gender, rol_num, course):
        super().__init__(name, age, gender)

        self.rol_num = rol_num

        self.course = course

    
    def display(self):

        super().display()
    
        print(f"roll num : {self.rol_num}, course : {self.course}")

person_01 = student("sharath", 21, "male", 123456, "python")

person_01.display()




    


        