# The first way to remove an item from a dictionary is the pop() method.
dict1 = {
    "Character" : "Batman",
    "Villian" : "Joker",
    "Rivals" : True,
}
dict1.pop("Rivals")
print(dict1)
# the popitem() method deleted the last vlaue added
dict1.popitem()
print(dict1)
# the del keyword deletd the item specifiec by the key word
del dict1[ "Character"]
print(dict1)
# And delete the whole dicitonary
del dict1
# clear () mehtod empties the dictionary
