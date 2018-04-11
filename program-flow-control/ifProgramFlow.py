name = input("Please enter your name: ")

# int makes sure that the following variable will be an integer as they
# are strings by default
age = int(input("How old are you, {0}? ".format(name)))

if age >= 18:
    print("You are old enough to vote")
else:
    print("Please come back in {0} years".format(18 - age))


print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess < 5:
    print("Please guess higher")
    guess = int(input())
    if guess == 5:
        print("Well done, you guessed it")
    else:
        print("Sorry, that is incorrect")

# elif = else if

elif guess > 5:
    print("Please guess lower")
    guess = int(input())
    if guess == 5:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly")
else:
    print("You got it right the first time")

# refactored

print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess != 5:
    if guess < 5:
        print("Please guess higher")
    else:
        print("Please guess lower")

    guess = int(input())
    if guess == 5:
        print("Well done, you got it!")
    else:
        print("Sorry, you have not guessed correctly")

else:
    print("You got it first time")