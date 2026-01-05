# In multiple inheritance, one child class inherits features from multiple parent classes.” 

class Father:

    def father_skill(self):

        print("driving skill")


class Mother:

    def mother_skill(self):

        print("cokking skill")

class Child(Father,Mother):

    pass

child_instance = Child()

child_instance.father_skill()
child_instance.mother_skill()