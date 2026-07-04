# you cannot copy a dictioanry by making dict2 = dict 1 because it will just refer to dict 1 
dict1 = {
    "Place"  : "France",
    "Time" : 12.34,
    "Fictional" : False,
}
print(dict1)
dict2 = dict1.copy()
print(dict2)
# you can also use th dict() fucntion to copy
dict3 = dict(dict1)
print(dict3)