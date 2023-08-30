import random
import time

print("\n*******************\n Number Guess Game\n*******************")
print("\n*******************************\n Please guess numbers from 1-40\n*******************************")


random_number = random.randint(1,40)
guess_right = 7

while True:

    guess = int(input("\nYour Guess: "))

    if (guess < random_number):
        print("Information is being questioned...")
        time.sleep(1)

        print("Please guess a more high number...")

        guess_right -= 1

        print("Remaining guess: ", guess_right)


    elif (guess > random_number):
        print("Information is being questioned...")
        time.sleep(1)

        print("Please guess a more lower number...")

        guess_right -=1

        print("Remaining guess: ",guess_right)

    else:
        print("Information is being questioned...")
        time.sleep(1)

        print("Congratulations! Your Number: ",random_number)
        break

    if (guess_right == 0):
        print("Your guess is over..")
        print("Your Number: ", random_number)
        break












