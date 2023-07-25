

print("\n**************************\nBody Mass Index Calculator\n**************************")


w = int(input("Weight: "))
h = float(input("Height: "))

index = w / (h ** 2 )

if (index < 18.5):
    print("Your Index: {}. You Are Weak".format(index))

elif (index >= 18.5 and index < 25):
    print("Your Index: {}. You Are Normal".format(index))

elif (index >= 25 and index < 30):
    print("Your Index: {}. You Are Fat".format(index))

else:
    print("Your Index: {}. You Are Obese".format(index))
