class Employee:

    id : int

    department : str

    salary : int

    def __init__(self, id, department, salary):

        self.id = id

        self.department = department

        self.salary = salary


    def display(self):

        print(f"Employee id : {self.id} Employee Department : {self.department} Employee salary : {self.salary} ")

class Developer(Employee):

    programming_language : str

    framework : str
    

    def __init__(self, id, department, salary, programming_language, framework):
        super().__init__(id, department, salary)

        self.programming_language = programming_language

        self.framework = framework

    def display(self): # method overridding, same method name (display) in parent and child 
        super().display()

        print(f"Language : {self.programming_language} frame work : {self.framework}")

emoloyee_01 = Developer(123456, "Prt", 30000, "python", "django")

emoloyee_01.display()



