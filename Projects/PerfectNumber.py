

print("\n           ******************************\n           ******* Perfect Number *******\n           ******************************\n")


number = int(input("Please Enter Number: "))

i = 1
total = 0
while (i < number):
    if (number % i == 0):
        total += i
    i += 1
if (total == number):
    print("Number is Perfect.")
    
else:
    print ("Number is not perfect.")
