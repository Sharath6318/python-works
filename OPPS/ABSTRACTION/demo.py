#Decoratot - > add a extra future to the function  but dont not change the defination of already define function 

# change a class into abstract class -> the class shoud be inherit form ABC(Abstract Base class)

# change the method into abstract method -> Apply @abstractmethod decorator


# car(start, stop, accelerate)

from abc import ABC, abstractmethod

class Car(ABC):
    
    @abstractmethod  # -----> apply abstractmethod decorator
    def start(self):

        pass

    @abstractmethod
    def stop(self):

        pass

    @abstractmethod
    def accelarate(self):

        pass


class Swift(Car):

    def start(self):

        print("swift is starting")

    def stop(self):

        print("Swift got stop")

    def accelarate(self):

        print("Swift get accelerate")

swift_instance = Swift()

swift_instance.start()
swift_instance.stop()  