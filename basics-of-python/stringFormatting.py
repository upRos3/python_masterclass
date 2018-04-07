age = 25

# allows you to concat an int by converting into a string
print("My age is " + str(age) + " years")

# replacement fields
print("My age is {0} years".format(age))

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}".format(31, "Jan", "March", "May",
                                                                          "July", "Aug", "Oct", "Dec"))

print("""Jan: {2}
Feb: {0}
March: {2}
April: {1}
May: {2}
June: {1}
July: {2}
Aug: {2}
Sept: {1}
Oct: {2}
Nov: {1}
Dec: {2}""".format(28, 30, 31))

# this is a deprecated, from python2
# --------------------------------------------

print("My age is %d years" % age)
print("My age is %d %s, %d %s" % (age, "years", 4, "months"))

for i in range(1, 12):
    # ** is to raise a number to the power of another
    # the 2 and 4 are to allocate up to 2 or 4 spaces in between for nicer formatting of the print
    print("No. %2d squared is %4d and cubed is %4d" % (i, i ** 2, i ** 3))

# you can use to format decimal as well
# f = Fixed point. Displays the number as a fixed-point number. The default precision is 6.
print("Pi is approximately %f" % (22 / 7))

print("Pi is approximately %.50f" % (22 / 7))

# --------------------------------------------

# the same in Python3

for i in range(1, 12):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i ** 2, i ** 3))

# in this case the f makes sure it is to 50 and not 'up to' 50 (49)
print("Pi is approximately {0:.50f}".format(22 / 7))

# no need for declaring a number of which arg, python can assume if not placed
# however, you can't use a value more than once

for i in range(1, 12):
    print("No. {:2} squared is {:4} and cubed is {:4}".format(i, i ** 2, i ** 3))

