

print("\n      **************************************\n      ******* Find Factorial Program *******\n      **************************************\n")

print("For exit the program, press 'q'\n ")

while True:
    number = input("Number: ")
    if (number == "q"):
        print("We are waiting for you again.")
        break
    number = int(number)

    factoriel = 1
    for i in range(2,number+1):
        factoriel *= i
    print("Factoriel: ",factoriel)