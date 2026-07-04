"""
Dictioinaries store data values in key:value pairs.
They are collections whihc are unoredered, chnageable and do not allow duplicates"""
dict1 = {
    "Character" : "Dante",
    "Son" : "Nero",
    "Name" : "Vergil",
}
print(dict1)
print(dict1["Name"])
# items can be reffered to by the key name, inside a square brakcet.
#we can add and remove items from dictioniaries.
#Again the use of the len() fucntion can tell us the length of the dictioniary.
print(len(dict1))
# Note you cannot have the samekey name in a dictionary otherwise it will overide the last value
# Dicitionaries can be any data type,
dict2 = {
    "Character" : "Dante",
    "Age" : 30,
    "Protagonist" : True,
}
print(dict2)
print(len(dict2))
print(dict2["Age"])
print(type(dict2))
# There is also a dict constructor that can make a dictionary from a list of tuples.
dict3 = dict((("name", "Ichigo"), ("age", 17), ("protag", True)))
print(dict3)
print(type(dict3))