# a for loop is used for iterating over a sequence
# WITH A FOR LOOP WE CAN EXECUTE A SET OF STATMENTS, ONCE FOR EACH ITEM IN A LIST, TUPLE OR SET OR DICTIONARIES.
Spell = ["Fire", "Water", "Ice"]
for x in Spell:
    print(x)
    print(type(Spell))
# Strings are also iterable objects
x = "Dante"
for x in "Dante":
    print(x)
# The break statment can end a for loop
Attacks = {"Punch", "Kick", "Super"}
for x in Attacks:
    print(x)
    if x in x == "Kick":
        break
# Continue again ends the current iteration and beggins a new one
for x in range(6):
    print(x)
# Note that rnag is 0 to 5 not 6
""" You can also add parameters to the ranges if they are integers"""
for x in range(1, 7):
    print(x)
for x in range(1, 10, 100):
    print(x)
""" Like the other fucntions you can also nets for loops use th pass statments nad use the else()"""
for x in range(10):
    if x == 5:
        break
        print(x)
    else: 
        print("I am done")