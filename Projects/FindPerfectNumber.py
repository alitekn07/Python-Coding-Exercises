print("\n**************************\nPerfect Number Finder\n**************************")



def perfectnumberfinder(number):

    total = 0

    for i in range(1,number):
        if (number % i == 0):
            total += i
    return total == number

for i in range(1,1001):
    if (perfectnumberfinder(i)):
        print("Perfect Number",i)