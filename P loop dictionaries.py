# You can also put a dictionart through a for loop to get the key and value pairs
# The returned values are the key but there are methods to return values aswell
dict1 = {
    "Place" : "Earth",
    "Time" : 10.30, 
}

for x in dict1:
    print(x)
    for x in dict1:
        print(dict1[x])

# the value method returns values
for x in dict1.values():
    print(x)
# for the key use key()
for x in dict1.keys():
    print(x)
# to loop through both keys and values use the items() method
for x,y in dict1.items():
    
    print(x,y)