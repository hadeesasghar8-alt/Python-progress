""" 
Sets are used to store multiple items in a single variable
A set is a collection which is unordered, unchangeable, and unindexed."""
# Also are written in curly brackets {}
Names = {"Dante", "Vergil", "Nero"}
print(Names)
# Set items are unordered, unchangeable and do not allow duplicate values.
names2 = {"Dante", "Vergil", "Nero", "Dante"}
print(names2)
#Length of a set again is doen using the len() fucntion
print(len(names2))
#set items can be any data type: boolean, int and string
set1 = {"Goku", "Vegeta", "Gohan"}
set2 = {1, 2 ,3 ,4 ,6}
set3 = {True, False, False, True}
# A set can contian mutliple data types
set4 = {"Goku", 1, False}
print(set4)
# P sees sets as objects with the data type "set"
print(type(set4))
#You can also use the set() constructor to make a set
set5 = set(("Picollo", 1, False))
print(set5)