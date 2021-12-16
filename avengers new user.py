from click import password_option


def new_user(fname, lname, uname, psswrd):
    print("Hello new user please enter your first and last name")
    print(fname, lname)
    print("Hello ", fname, lname, ", please enter your username.")
    valid_uname = len(uname) >= 8 
    while not valid_uname:
        print("Username is invalid, try again...")
        print("Please choose a username with atleast 8 characters. ")
        break
    else: 
        print("Welcome " + uname)
    print("Hello " + uname + ", please select a strong password. ")
    valid_psswrd = len(psswrd) >= 10
    while not valid_psswrd:
        print("Password is invalid, try again...")
        print("Please enter a password with 10+ characters. ")
        break
    else: 
        print("You're password is " + psswrd)
    print("Now we will be setting up your secure keyring")
    keyring = ((id(uname) * len(psswrd)) ** 3.1415) *100 
    print("You're keyring is " + str(keyring))
    print("Do not share you're keyring with anyone")
    pin = (id(psswrd) + id(fname)) // 9.8
    print("You're card pin is: ", pin)


new_user("steve", "rogers", "Cptn", "Rogers") 
new_user("Bruce", "Banner", "Hulk", "smash")
new_user("Steve", "Rogers", "Captain_America", "americaamericaamerica")
new_user("Thor", "Son of Odin", "Thor_Odinson", "Strongest avenger")
new_user("Tony", "Stark", "Ironman", "ironmanmkv")