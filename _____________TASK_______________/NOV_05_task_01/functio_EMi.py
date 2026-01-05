total_amount = int(input("Enter the total amount :"))
total_interest = int(input("Enter the total interest :"))
tenure = int(input("Enter the time periode :"))

def Emi(a, i, r):

    monthly_interest = i / (12 * 100)

    monthly_T = r * 12

    monthly_emi = ( a * monthly_interest * (1 + monthly_interest) ** monthly_T ) / ( (1 + monthly_interest) ** monthly_T - 1 )

    return monthly_emi

monthly_emi = Emi(total_amount,total_interest,tenure)

print(f"your monthly EMI {round(monthly_emi)}")

    

    