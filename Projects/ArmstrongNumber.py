

print("\n           ********************************\n           ******* Armstrong Number *******\n           ********************************\n")


Number = input("Number: ")
Number0fDigits = len(Number)
Number = int(Number)
Digit = 0
Total = 0

TemporaryNumber = Number

while (TemporaryNumber > 0):
    Digit = TemporaryNumber % 10
    Total += Digit ** Number0fDigits
    TemporaryNumber //= 10

if (Total == Number):
    print("This Number is Armstrong")
else:
    print("This Number isn't Armstrong")