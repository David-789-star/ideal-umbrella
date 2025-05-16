
# What is condition?
# What is statement?

'''
Condition means something should exist before something can happen

Statement is a complete instruction or command that python interpreter can execute

A statement that can be true or false
'''

'''
username, password
'''

usernames = ["Temitopefx", "SamsonDrums", "DaniellaNoise"]
passwords = ["Password@1$", "Gateway22", "Qwerty.6"]

while True:
    username = input("Enter Username: ") 
    password = input("Enter Password: ")
    
    if username in usernames:
    	index = usernames.index(username)
    	if password == passwords[index]:
    		print(f"Welcome {username}")
    else:
        print("Incorrect Password!!")
else:
    print("Incorrect Username!!")
