import random

incorrect = True
turns = 1
maxNum = 100

number = random.randint(1, maxNum)
while incorrect:
    guess = int(input("Guess a number between 1 and " + str(maxNum) + ": "))
    if guess == number:
        print("\nWell done you have guessed correctly")
        print("The number generated was: ", number)
        incorrect = False
    else:
        print("Incorrect, try again")
        if guess < number:
            print("Higher!")
        else:
            print("Lower!")
        turns = turns + 1


print("Number of turns:", turns)
