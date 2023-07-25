print("\nGamer Save Program V1\n")

Name = input("Please enter the name :")
Surname = input("Please enter the surname :")
Team = input("Is the player in the Red team or the Blue team ? :")

Informations = [Name, Surname, Team]


print("The informations are saving....")

print(f"Gamer Name: {Name}\nGamer Surname: {Surname}\nGamer Team: {Team}\n".format(Informations[0],Informations[1],Informations[2]))


print("The Informations are Saved..")
