age = int(input("Enter the age : "))


if age < 18:

    raise Exception("Invalid age")

else:

    print("Eligible for voting")