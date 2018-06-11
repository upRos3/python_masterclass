number = "9,223,372,036,854,775,807"
cleanedNumber = ''

# Using augmented assignments in Python is more efficient (+= -= *= etc)
for i in range(0, len(number)):
    if number[i] in '0123456789':
        cleanedNumber += number[i]

newNumber = int(cleanedNumber)
print("The number is {} ".format(newNumber))

x = 23
x += 1
# 24
print(x)

x -= 4
# 20
print(x)

x *= 5
# 100
print(x)

x /= 4
# 25.0
print(x)

x **= 2
# 625.0
print(x)

x %= 60
# 25.0
print(x)

greeting = "Good "
greeting += "morning "
print(greeting)

greeting *= 5
print(greeting)