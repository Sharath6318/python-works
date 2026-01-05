
            # EMI Calculation 


P = float(input("Enter the total amount :"))

R = float(input("Enter the anual intrest :"))

N = float(input("Enter Time period in Year :"))

monthly_R = R / (12 * 100)

monthly_N = N * 12

EMI_amount =( P * monthly_R * (1 + monthly_R) ** monthly_N ) / ( (1 + monthly_R) ** monthly_N - 1 )

print("Monthly EMI of your loan amount", round(EMI_amount,2))

emi = ( P * monthly_R * (1 +monthly_R) ** monthly_N) /((1 + monthly_R) ** monthly_N - 1)