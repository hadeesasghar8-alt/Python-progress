"""
You can also remove items from a set with the remove(), discard() methods"""
set1 = {"Goku", "Vegeta", "Gohan", "Picollo"}
set1.remove("Picollo")
print(set1)
set1.discard("Goku")
print(set1)
# You can also use pop() method but it will remove a random item from the set
set2 = {"Ichigo", "Rukia", "Renji"}
x = set2.pop()
print(x)
print(set2)
# the clear() method clears the set
set2.clear()
print(set2)
# del() will delete it all
del set2