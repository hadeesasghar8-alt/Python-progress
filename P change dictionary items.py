# You can change items by referring tot he key name.
dict1 = {
    "Place" : "Earth",
    "Time" : 10.30,
    "colour" : "blue",
}
print(dict1)
dict1.update({"Place" : "Namek"})
print(dict1)
#The update() method lets update the dicitonaries 
# you can also just refer to the key name then do it
dict1["Time"] = 11.30
print(dict1)