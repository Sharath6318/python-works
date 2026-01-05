age = int(input("Enter your age :"))

if age >= 18 :
    
    test_res = input("Enter test result :")

    if test_res == "pass":

        print("Licence Aproved")

    elif test_res == "fail":

        print("Licence NOT Aproved")

else:

    print("Not eligible due to age")




