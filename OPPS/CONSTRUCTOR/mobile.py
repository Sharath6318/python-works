class Mobile():

    title : str

    price : int

    brand : str

    features : str

    def __init__(self, title, price, brand, features): # Constructor

        self.title = title

        self.price = price

        self.brand = brand

        self.features = features


    def diplay_details(self):

        print(f"Mobile title : {self.title}")

        print(f"Mobile price : {self.price}")

        print(f"Mobile brand : {self.brand}")

        print(f"Mobile features : {self.features}")


mobile_01 = Mobile("IQOO Z5", 18000, "VEVO", "GAMMING")

mobile_02 = Mobile("Samsung s25", 150000, "Samsung", "Ai Camera")

mobile_01.diplay_details()

mobile_02.diplay_details()