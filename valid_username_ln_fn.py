def new_user(first_name, last_name, username, password):
    print("Hello " + last_name + ", " + first_name + " please enter a valid username and password")
    valid_username = len(username) > 6
    while not valid_username:
        print("Username Invalid. Try again...")
        break
    else:
        print("Username: " + username)
    valid_password = len(password) > 8
    while not valid_password:
        print("Password Invalid. Try again...")
        break
    else:
        print("Password: " + password)
        

new_user("Charles", "Agnew", "chri", "anglebottom")
new_user("Kirk", "Kanklebottem", "Serpent", "strongtow")