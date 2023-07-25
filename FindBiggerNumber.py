
print("\n**************************\nFind Bigger Number\n**************************")


a = int(input("First Number: "))
b = int(input("Second Number: "))
c = int(input("Third Number: "))

if (a>b and a>c):

    print("{} number is biggest.".format(a))

elif (b>a and b>c):

    print("{} number is the biggest.".format(b))

elif (c>a and c>b):

    print("{} number is the biggest.".format(c))

elif (a>=b and a>=c or c>=a and c>=b or b>=a and b>=c):

    print("There are multi big numbers.")