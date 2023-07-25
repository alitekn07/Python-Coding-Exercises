

print("Saving Information\n")

Name = input("Enter Name: ")
Surname = input("Enter Surname: ")
Number = int(input("Enter Number: "))

Informations = [Name, Surname, Number]

print("\nInformations are saving..\n")

print(f"Name: {Name}\nSurname: {Surname}\nNumber: {Number}".format(Informations[0], Informations[1],Informations [2]))

