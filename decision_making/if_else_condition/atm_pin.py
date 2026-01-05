user_pin = 123456

balance = 6000

pin = int(input("Enter you password :"))

if user_pin == pin:

    amount = int(input("Enter the amount :"))

    if amount <= balance :

        print("transition sucessfully")

    else:

        print("transition incomplete")

else:

    print("incorrect pin")