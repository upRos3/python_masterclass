parrot = "Norwegian Blue"
print(parrot)
print(parrot[0])
print(parrot[3])
print(parrot[-1])
print(parrot[0:6])

# will start from beginning of string
print(parrot[:6])

# will start from index 6 till end
print(parrot[6:])

# can also go backwards
print(parrot[-4:-2])

# slicing everything from index 0 - 6 (non inclusive) in steps of 2
print(parrot[0:6:2])

print(parrot[0:6:3])

# extended slices

number = "9,232,432,432,543,321,543,321"
print(number[1::4])

numbers = "1, 2, 3, 4, 5, 6, 7, 8, 9"
print(numbers[0::3])

string1 = "Hello "
string2 = "Wor"
print(string1 + string2)

# python does not require you to concat strings directly (ie not in a variable)
print("Hello " "Wor" "ld")

# you can multiply strings too
print("Hello " * 5)
print("Hello " * (5 + 4))

#Can still concat
print("Hello " * 5 + "World")

# Can search a substring of a string, returns boolean
today = "Saturday"
print("day" in today)
print("fri" in today)
