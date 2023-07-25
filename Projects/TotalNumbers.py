

print("\n           ****************************\n           ******* Total Numbers ******\n           ****************************\n")


Total = 0

while True:
    number = input("Number: ")

    if (number == "q"):
        break
    number = int(number)

    Total += number

print("Total of your numbers: {}".format(Total))