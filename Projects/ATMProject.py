
print("\nWelcome To TEKIN Bank\n")

print("\nMr. ALI TEKIN\n")

print("""Please Select To What Do You Want To Do ?

1. Balance Inquiry
2. Deposit
3. Withdraw
4. Exit

""")

balance = 100000

while True:
    process = input("Please enter the process: ")

    if (process == "4"):
        print("\nSee You Soon..")
        break

    elif (process == "1"):
        print("\nYour balance is: {} $".format(balance))

    elif (process == "2"):
        amount = int(input("\nThe amount you want to deposit: "))
        balance += amount
        print("Balance Updated: {} $".format(balance))
    elif (process == "3"):
        amount = int(input("\nThe amount you want to withdraw: "))
        if (balance - amount < 0):
            print("Error..\nInsufficient balance")
            print("\nYour balance is: {} $".format(balance))
            continue
        balance -= amount
        print("Available balance: {} $".format(balance))
    else:
        print("Please enter a valid transaction..")
