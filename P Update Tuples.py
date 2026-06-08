#Tuples are unchangeable but there are workarounds.
# If you convert tuples into lists then comvert the list back into a tuple
x = ("Dante", "Nero", "Vergil" )
y = list(x)
y[1] = "Mary"
x = tuple(y)
print(x)
#The smae method can be used to add items into the tuple with append() function.
newtuple = ("Goku", "Gohan", "Vegeta")
y = list(newtuple)
y.append("Piccolo")
newtuple = tuple(y)
print(newtuple)
# You can also add a tuple to a tuple no matter the length of the tuple
thistuple = ("Goku", "Gohan")
y = ("Goten",)
thistuple += y
print(thistuple)
# you can also remove items
newesttuple = ("apple", "pear", "orange")
y = list(newesttuple)
y.remove("pear")
newesttuple = tuple(y)
print(newesttuple)
# to delete a tuple u can use the del function 
