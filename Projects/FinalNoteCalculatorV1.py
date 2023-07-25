
print("************************\nFinal Note Calculator V1\n************************\n")


visa = int(input("Enter Visa Note: "))
final = int(input("Enter Final Note: "))

general_note =  visa * 25/100 + final * 75/100

if (general_note >= 90):
    print("\nYour Note Is: {}\nLetter grade: AA".format(general_note))

elif (general_note >= 85):
    print("\nYour Note Is: {}\nLetter grade: BA".format(general_note))

elif (general_note >= 80):
    print("\nYour Note Is: {}\nLetter grade: BB".format(general_note))

elif (general_note >=75):
    print("\nYour Note Is: {}\nLetter grade: CB".format(general_note))

elif (general_note >= 65):
    print("\nYour Note Is: {}\nLetter grade: CC".format(general_note))

elif (general_note >= 58):
    print("\nYour Note Is: {}\nLetter grade: DC".format(general_note))

elif (general_note >= 50):
    print("\nYour Note Is: {}\nLetter grade: DD".format(general_note))

elif (general_note >= 40):
    print("\nYour Note Is: {}\nLetter grade: FD".format(general_note))

else:
    print("\nYour Note Is: {}\nLetter grade: FF".format(general_note))
