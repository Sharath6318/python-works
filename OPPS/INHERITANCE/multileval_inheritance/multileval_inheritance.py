# In multilevel inheritance, a class is derived from another derived class, forming a chain of inheritance.”

class GrandParent:

    def properties(self):

        print("50 cent land and huge vintage home")

class Parent(GrandParent):

    def car(self):

        print("hundai car")

class Child(Parent):

    def gadgets(self):

        print("iphone laptop ipad")

child_instance = Child()

child_instance.properties()
child_instance.car()
child_instance.gadgets()