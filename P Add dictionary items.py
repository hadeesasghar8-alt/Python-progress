# adding items can be done using a new index key and assinging a value to it.
dict1 = {
    "Place" : "Gotham",
    "Time" : 11.31,
    "Fictional" : True,
}
print(dict1)
dict1["Villian"] = "Joker"
print(dict1)
dict1.update({"Hero" : "Batman"})
print(dict1)
# Note that the update() method also works 
