

print("\n           *******************************\n           ******* User Login Page *******\n           *******************************\n")

sys_username = "alitekn07"
sys_password  = "123456"

right_of_entry = 3

while True:
    username = input("\nUsername: ")
    password = input("Password: ")

    if (username != sys_username and password == sys_password):
        print("Wrong Username..")
        right_of_entry -= 1
        print("Right Of Entry: ",right_of_entry)

    elif (username == sys_username and password != sys_password):
        print("Wrong Password..")
        right_of_entry -= 1
        print("Right Of Entry: ", right_of_entry)

    elif (username != sys_username and password != sys_password):
        print("Wrong Username or Password..")
        right_of_entry -= 1
        print("Right Of Entry: ", right_of_entry)

    else:
        print("\nLogged In Succesfully..")
        break

    if (right_of_entry == 0):
        print("\nYOU ARE BLOCKED!")
        break