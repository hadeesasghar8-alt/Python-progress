#  A dictionaries can contian other dictionaries,menaing they are Nested dictionaries.
dict1 = {
    "Place1" : {
        "Country" : "Wakanda",
        "Time" : 10.30,
        "Year" : 2023,
    },
    "Place2" : {
        "Planet" : "Namek",
        "Time" : 11.30,
        "Year" : 2024,
    },
    "Place3" : {
        "Person" : "Goku",
        "Planet" : "Earth",
        "Time" : 12.30,
    }
}
print(dict1)
# or create three seperatre dictionaries tthen add them to a big new one.
dict2 = {
    "name" : "Ichigo",
    "age" : 15,
}
dict3 = {
    "name" : "Rukia",
    "age" : 14,
}
Bleach = {
    "charcter1" : dict2,
    "character2" : dict3,
}
print(Bleach)
# AGin you can access items in nested dictionaries by refering to key names
print(Bleach["charcter1"]["name"])
# or loop them through a for loop
for x in Bleach.items():
    print(x)