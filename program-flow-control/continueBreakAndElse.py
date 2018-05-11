shopping_list = ["milk", "eggs", "spam", "bread", "rice"]

# Continue stops processing any item called spam but continues iterating through list

for item in shopping_list:
    if item == 'spam':
        continue

    print("Buy " + item)

print("==============")

# Break escapes the loop completely after it is called

for item in shopping_list:
    if item == 'spam':
        break

    print("Buy " + item)

print("==============")

# Note: Else can follow both a for and if statement. Reason for indentation like so:

meal = ["egg", "bacon", "beans", "sausages"]
nasty_food_item = ""

for item in meal:
    if item == 'spam':
        nasty_food_item = item
        break
else:
    print("I'll have a plate of that, then, please!")

if nasty_food_item:
    print("Can't I have anything without spam in it?!")

# Python does not have strict convention on naming variables, you can use snake case or
# camel case but be consistent. It is also case sensitive.
