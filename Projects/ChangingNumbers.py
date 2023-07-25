
print("Changing Numbers")

s1 = int(input("Enter Number 1: "))
s2 = int(input("Enter Number 2: "))

print("Values Before Changing\na: {} b: {}\n".format(s1,s2))

s1, s2 = s2, s1

print("Values After Changing\na: {} b: {}\n".format(s1,s2))