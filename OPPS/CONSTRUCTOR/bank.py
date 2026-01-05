class Bank():

    acc_num : int

    name : str

    acc_type : str

    balance : int


    def __init__(self, acc_num, name, acc_type, balance): # method

        self.acc_num = acc_num
        
        self.name = name

        self.acc_type = acc_type

        self.balance = balance

    def deposit(self,amount):

        self.balance += amount

        print(f"your account {self.acc_num} creadted {amount} and your balance is {self.balance}")

    def withdraw(self,amount):

        if amount < self.balance:

            self.balance -= amount

            print(f"your account {self.acc_num} debited {amount} and your balance is {self.balance}")

        else:

            print("transaction faild insufficient balance")

    def mainbalance(self):

        print(f"hai {self.name} your acc bal is {self.balance}")


bank_instance_01 = Bank(12345, "sharath", "0bal", 10000)

# bank_instance_01.set_account(12345, "sharath", "0bal", 10000)

bank_instance_01.deposit(10000)

bank_instance_01.mainbalance()

