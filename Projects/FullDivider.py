print("\n**************************\n      Full Divider\n**************************")


def findfulldivider(number):
    full_dividers = []

    for i in range(2,number):
        if (number % i == 0):
            full_dividers.append(i)
    return full_dividers

while True:
    number = input("Please enter number or for quit press 'Q'\nNumber:")

    if (number == "q" or number == "Q"):
        print("The Program Ended..")
        break
    else:
        number = int(number)
        print("Full Divider: ",findfulldivider(number))
