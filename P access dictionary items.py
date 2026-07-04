"""
you can access dicitonary items by refering to thier key names
"""
dict1 = {
    "Character" : "Goku",
    "Age" : 40, 
    "Protag" : True,

}
print(dict1)
print(dict1["Protag"])
x = dict1.get("Age")
print(x)
# the get() method allows for the same result
# The key() method will reurn all the keys in the dictionary as a list.
print(dict1.keys())
# The lsit of keys in a dictionary are a view of it menaing any changes to done will be reflected in the key lists.
dict1["Age"] = 41
print(dict1)
y = dict1.values()
print(y)
# values() method reurns the values.
# The list of values is a view of the dicitonary and any changes to the dictionary will be reflected in the values list.
dict1["Race"] = "Saiyan"
print(dict1)
# the items () mehtod will return a list of tuples containg teh key value pairs
l = dict1.items()
print(l)
# To check if keys ecist use the in key word.
if "Character" in dict1:
    print("Yes, it exists")
    