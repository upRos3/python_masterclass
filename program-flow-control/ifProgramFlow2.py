age = int(input("How old are you? "))

# if (age >= 16) and (age <= 65):

# can be refactored to:

# if 16 <= age <= 65:
#     print("Have a good day at work")

if 16 < age > 65:
    print("Enjoy your free time")
else:
    print("Have a good day at work")

# Python does not have a boolean data type but instead has two constants true or false
# for example:

x = "false"

if x:
    print("x is true")

# comes back as true

# python 1 = true, 0 = false but in a condition any non 0 or non empty value is true

x = input("Please enter some text: ")

if x:
    print("You entered '{}'".format(x))
else:
    print("You did not enter anything")

# not reverses a true or false value

print(not False)
print(not True)

age = int(input("How old are you? "))

if not(age < 18):
    print("You are old enough to vote")
    print("Please put an x in the box")
else:
    print("Please come back in {0} years".format(18 - age))

# in is used in sequences

parrot = "Norwegian Blue"

letter = input("Enter a character: ")

if letter not in parrot:
    print("I don't need that letter")
else:
    print("Give me an {}, Bob".format(letter))

# If I use a b, it will not be 'in' the string as it is a capital.