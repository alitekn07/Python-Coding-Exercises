

print("******************\nUser Login System\n******************")

sys_username = "alitekn07"
sys_password = "123456"

username = input("Username: ")
password = input("Password: ")

if (username == sys_username and password != sys_password):
    print("\nWrong Password!")

elif (username != sys_username and password == sys_password):
    print("\nWrong Username!")

elif (username != sys_username and password != sys_password):
    print("\nWrong Username and password!")

else:
    print("\nYou have successfully logged in!")