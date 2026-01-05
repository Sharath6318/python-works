
from abc import ABC, abstractmethod

class Editor(ABC):

    @abstractmethod    
    def create_module_package(self):

        pass
    @abstractmethod
    def edit(self):

        pass
    @abstractmethod
    def execute(self):

        pass
    @abstractmethod
    def debug(sefl):

        pass

class VsCode(Editor):

    def create_module_package(self):

        print("vs code create modules and packages")

    def edit(self):

        print("vs code have edit option")


    def execute(self):

        print("Vs code have execute option")

    def debug(sefl):

        print("Vs code have dubug option")

class Pycharm(Editor):

    def create_module_package(self):

        print("Pycharm create modules and packages")

    def edit(self):

        print("Pycharm have edit option")


    def execute(self):

        print("Pycharm have execute option")

    def debug(sefl):

        print("Pycharm have dubug option")
        
vs_code_instance = VsCode()
Pycharm_instance = Pycharm()

vs_code_instance.execute()
Pycharm_instance.execute()


