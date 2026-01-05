# 


# * recive in tuple

class Calculator:

    def add(self, *args):

        print(sum(args))


new_instance = Calculator()

new_instance.add(10, 20)
new_instance.add(10, 20, 30)

#  ** recive in dict

def display_person(**kwargs):

    print(kwargs)


display_person(name = "hair", age = 21, place = "thrissur", salary = "28000")




        
