class Frameword():

    name : str
     
    language : str
     
    architecutre : str


    def set_framework(self, name, language, architecture): # our method

        self.name = name

        self.language = language

        self.architecutre = architecture


    def display(self):

        print(self.name, self.language, self.architecutre)

frame_wrk_inst_01 = Frameword() # create a object

frame_wrk_inst_01.set_framework("django", "python", "same")

frame_wrk_inst_01.display()