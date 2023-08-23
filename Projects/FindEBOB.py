print("\n**************************\nEBOB Finder\n**************************")


def find_ebob(number1,number2):

    i = 1
    ebob = 1

    while(i <= number1 and i <= number2):

        if (not (number1 % i) and not (number2 % i)):
            ebob = i

        i += 1
    return ebob
number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))

print("Ebob: ",find_ebob(number1,number2))