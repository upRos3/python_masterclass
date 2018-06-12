# i = 0
# while i < 10:
#     print("i is now {}".format(i))
#     i += 1
#

# While loops are good for situations where you need to stay within the loop until
# a certain condition is met. Unlike a for loop, you do not need to know how many
# times the loop will execute.

available_exits = ["east", "north east", "south"]

chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit == "quit":
        print("Game Over")
        break

else:
    print("aren't you glad you got out of there!")

# ============================================

# coming back to the number guessing game that was made in the ifProgramFlow, a while
# loop would have been a better way to implement the game as this only gives us two chances
# to guess the number.

# this imports a function to produce a random int
import random

highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}: ".format(highest))
guess = int(input())
if guess != answer:
    if guess < answer:
        print("Please guess higher")
    else:  # guess must be greater than number
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly")
else:
    print("You got it first time")

# the next challenge is to modify this code to use a while loop to allow as many guesses
# as needed

