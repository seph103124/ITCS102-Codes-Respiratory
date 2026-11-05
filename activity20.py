from getpass import getpass

u = "asas2a1"
p = "1234"

isLogin = False
while isLogin == False:
    user = input("Enter your username --->  ")
    password = getpass("Enter your password --->  ")
    if user == u and password == p:
        print("Login successful!")
        isLogin = True
    else:
        print("Invalid username or password.Please try again.")
        isLogin = False