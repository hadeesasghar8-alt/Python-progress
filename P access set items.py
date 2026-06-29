# You cannot access items in a set by referring to and index or a key.
# But using a for loop you can loop through the set items, or ask for specific value by using the in key word.
thisset = {"Dante", "Vergil", "Nero"}
for x in thisset:
    print(x) 
print("Dante" in thisset)
print("Dante" not in thisset)

