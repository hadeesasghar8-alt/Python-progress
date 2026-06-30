# You cannot chnage items in a set after its been created, but you can add new items.
# Use the add () method
set1 = {"Dante", "Vergil", "Nero"}
set1.add("V")
print(set1)
# To add itmes from another set into a set, you can use the update()
set2 = {"Goku", "Gohan", "Vegeta"}
set1.update(set2)
print(set1)
# The object in the update() method does not have to be in a set. It can be any iterable object.
mylist1 = ["Taniks"]
set1.update(mylist1)
print(set1)