from multiprocessing import managers


print("Welcome new Avenger, please enter your codename: ")
codename = input()
print("Hello {}, welcome to the Avengers Initiative".format(codename))
print("Enter your system name. ")
system_name = input()
print("Verify system name: {}".format(system_name))
print("Would you like to setup your account? Please enter y for yes or n for no")
setup = input()
if setup == "n":
    print("Exiting setup...")
if setup == "y" :
    print("Please enter your First and Last name")
    name = input()
    print("Govenment Name: {}".format(name)) 
    print("Now you need to setup a username and password")
    print("Your username must be atleast 8 characters.  Please enter your username. ")
    username = input()
    while len(username) < 8:
        print("Username: {} is invalid. Try again.".format(username))
        username = input()
    else:
        print("Your new username is: {}".format(username))
    print("Next we need to setup your password.  Your password must be atleast 10 characters. ")
    password = input()
    while len(password) < 10:
        print("Password is invalid.  Remember that passwords must be atleast 10 characters.  Please try again.")
        password = input()
    else:
        print("Your new password is: {}".format(password))
    print("Now we need to setup your Account Number and PIN")
    print("Your account number will be generated based on the information you provided...")
    account_number = ((id(username) * 3.14156) + len(password))
    print("Your account number is: {:.0f}".format(account_number))
    print("Please enter your PIN.  Your PIN should be a 4 digit code.  This will be used to access your account and card balance.")
    pin = input()
    while not pin.isnumeric() and len(pin) != 4 : 
        print("PIN must be numeric and exactly 4 digits.  User cannot enter alphabetic characters in PIN code.")
        pin = input()
    else:
        print("Your pin is: {}".format(pin))
print("Is there anything else you would like to do before exiting?")
print(["Setup tax information", "Check inbox", "Confirm address", "Confirm contact information"])
selection = input()
if selection == ("Setup tax information"):
    print("We will now begin setup of you I-9 and verify your w-2 from last tax year.")
if selection == ("Check inbox"):
     print("Checking inbox...")
if selection == ("Confirm address"):
    print("Enter home address")
if selection == ("Confirm contact information"):
        print("Please enter your phone number and email address.")