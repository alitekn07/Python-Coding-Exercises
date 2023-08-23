print("\n**************************\n       EKOK Finder\n**************************")


def find_ekok(number1,number2):

    i = 2
    ekok = 1

    while True:
        if (number1 % i == 0 and number2 % i == 0):
            ekok *= i

            number1 //= i
            number2 //= i

        elif (number1 % i == 0 and number2 % i != 0):
            ekok *= i

            number1 //= i

        elif (number1 % i != 0 and number2 % i == 0):
            ekok *= i

            number2 //= i

        else:
            i += 1
        if (number1 == 1 and number2 == 1):
            break
    return ekok

number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))

print("Ekok: ",find_ekok(number1,number2))