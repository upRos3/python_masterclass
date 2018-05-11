# for i in range(1, 20):
#     print("i is now {}".format(i))
#
# number = "9,223,372,036,854,775,807"
# for i in range(0, len(number)):
#     print(number[i])

number = "9,223,372,036,854,775,807"
cleanedNumber = ''

for i in range(0, len(number)):
    if number[i] in '0123456789':
        cleanedNumber += number[i]

newNumber = int(cleanedNumber)
print("The number is {}".format(newNumber))

# -------------- Part 2 -----------
# Extending for loops


# Reducing the amount of code, for loops assigns each character in the
# sequence number to a loop a loop variable character

number = "9,223,372,036,854,775,807"
cleanedNumber = ''

for char in number:
    if char in '0123456789':
        cleanedNumber += char

newNumber = int(cleanedNumber)
print("The number is {}".format(newNumber))

for state in ["not pinin'", "no more", "a stiff", "bereft of lift"]:
    print("This parrot is " + state)

# Stepping ranges

for i in range(0, 100, 5):
    print("i is {}".format(i))

# Nested for loops

for i in range(1, 13):
    for j in range(1, 13):
        print("{1} times {0} is {2}".format(i, j, i*j), end="\t")
    print("=============")
