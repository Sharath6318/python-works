class Rbi:

    def gold_loan_rate(self):

        print("Gold loan Rate", 8.5)

    def home_loan_rate(self):

        print("home loan Rate", 9.2)

    def car_loan_rate(self):

        print("car loan Rate", 9.5)

class Hdfc(Rbi):

    def gold_loan_rate(self):

        print("Gold loan Rate", 9.5)

    def home_loan_rate(self):

        print("home loan Rate", 10)

    def car_loan_rate(self):

        print("car loan Rate", 8.5)


new_hdfc_instance = Hdfc()
new_rbi_instance = Rbi()

new_hdfc_instance.gold_loan_rate()
new_hdfc_instance.home_loan_rate()
new_hdfc_instance.car_loan_rate()

