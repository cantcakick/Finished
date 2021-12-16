from click import password_option


def new_user(uname, psswrd):
    print("Hello new user, please enter your username. ")
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

new_user("steve", "rogers") 
new_user("Hulk", "smash")
new_user("Captain_America", "americaamericaamerica")
new_user("Thor_Odinson", "Strongest avenger")