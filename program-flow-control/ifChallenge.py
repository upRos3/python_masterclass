# Write a small program to ask for a name and age
# When both values have been entered, check if the person
# is the right age to go on an 18 - 30 holiday (they must be
# 18 or older and under 31).
# If they are, welcome them to the holiday, otherwise print
# a polite message refusing them entry.

name = input("Please tell me your name: ")
age = int(input("Please tell me your age: "))

if 17 < age < 31:
    print("Pack your bags {0}!".format(name))
else:
    print("Sorry {0}, you're not the right age for this holiday".format(name))
