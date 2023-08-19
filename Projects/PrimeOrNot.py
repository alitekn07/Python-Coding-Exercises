"""
Prime Numbers: Numbers that are not divisible by 1 and any other number.
"""


def is_it_prime (number):
    if (number == 1):
        return False

    elif (number == 2):
        return True

    else:
        for i in range(2,number):
            if (number % i == 0):
                return False
        return True

while True:
    number = input("Number:")

    if (number == "q"):
        break
    else:
        number = int(number)

        if (is_it_prime(number)):
            print(number, "This is Prime Number")
        else:
            print(number, "This is not Prime Number")