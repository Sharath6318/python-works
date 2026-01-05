passkey = 123456
otp = 582

password = int(input("Enter the password :"))

if(password == passkey):

    user_otp = int(input("Enter the otp: "))

    if(user_otp == otp):

        print("login sucessfully")

    else:

        print("incorrect otp")

else:

    print("incorrect password")