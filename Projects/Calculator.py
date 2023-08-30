import math
from time import sleep

print("\n                    ***********\n                    CALCULATOR\n                    ***********")

print("""
Please select the action to take..

0) Exit
1) Gathering (+)
2) Subtraction (-)
3) Multiplication (*)
4) Divide (/)
""")

while True:
    process = int(input("Please Select: "))

    if process == 0:
        print("Exiting the program please wait...\n")
        sleep(1)
        print("The program has been exited, have a nice day!")
        break

    elif process == 1:
        print("Please enter 2 number\n")

        a = int(input("First Number: "))
        b = int(input("Second Number: "))

        print("\nProcessing...")
        sleep(1)

        print("\nResult: ", a+b)

    elif process == 2:
        print("Please enter 2 number\n")

        a = int(input("First Number: "))
        b = int(input("Second Number: "))

        print("\nProcessing...")
        sleep(1)

        print("\nResult: ", a-b)

    elif process == 3:
        print("Please enter 2 number\n")

        a = int(input("First Number: "))
        b = int(input("Second Number: "))

        print("\nProcessing...")
        sleep(1)

        print("\nResult: ", a*b)

    elif process == 4:
        print("Please enter 2 number\n")

        a = int(input("First Number: "))
        b = int(input("Second Number: "))

        print("\nProcessing...")
        sleep(1)

        print("\nResult: ", a/b)

    else:
        print("\nWrong Selection..")
        print("Exiting the program..")
        break