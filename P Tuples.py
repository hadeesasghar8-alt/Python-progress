# Tuples are used to store multiple items into one variable
# Tuples are 1 of 4 bulit-in list types
# tuples are written with round brackets.
thisisatuple= ("Dante", "Vergil", "Nero")
print(thisisatuple)
"""
Tuple items are ordered, unchangeable, and allow for duplicate values
Tuple items are indexed, the first item has index [0], and the second is [1] etc.
Odered refers to tuples having a set order that cannot be changed.
They are unchangeable meaning after they are created no alterations can be made
and they allow duplicat evalues.
"""
newtuple = ("Goku", "Vegeta", "Gohan", "Goku")
print(newtuple)
# to determine length we use the len() function again.
print(len(newtuple))
# To make a tupple with only one item there must be a comma after the item
newesttuple = ("v",)
print(newesttuple)
# Tuples can hold dtata of any type string, int or booleans
#Tuples in python are defined as objects with the type "tuple"
print(type(newesttuple))
# the tuple() constructor can be used to creat tuples
Tuple = tuple(("car", "train"))
print(Tuple)
"""
The other list types include:
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
""" 