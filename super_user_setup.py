def super_user_setup(fname, lname, uname, pword):
    key = len((uname + lname)) ** 3.141579
    print ("Hello new Super User " + fname , lname + " we will now be setting up your account")
    if len(uname) > 7:
        print ("Your username is : " + uname )
    elif len(uname) < 7: 
        print ("Username must be atleast 7 characters")
    if len(pword) > 8:
        print ("Your password is : " + pword )
    elif len(pword) < 8:
        print ("Chosen password does not meet security requirements...")
    print ("Your key is : " + str(key) )
    
    
super_user_setup("Charles", "Agnew", "ChristianA", "Sumosumosumo")
    