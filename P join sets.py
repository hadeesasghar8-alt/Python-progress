# The union() method returns a new set from both the old sets
set1 = {"Goku", "Vegeta", "Gohan"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
# next one is |
set4 = set3 | set1
print(set4)
set5 = {"Kratos", "Clive", "Cloud"}
set6 = {4, 5, 7}
newset = set4.union(set5,set6)
print(newset)
# same result using the |
# you can use join tuple and sets 
y = ("Gintoki", "Kagura", "Shinpachi")
z = set1.union(y)
print(z)
#note the | operator only allows for set to set action
"""
The update() method adds new items into a set and does not make a new set"""
set1.update(set6)
print(set1)
#Both union() and update() methos exclude duplicates
#Whereas intersection only return a new set with duplicates items in different sets
set7 = {"Goku", "Lady", "Trish"}
set8 = set1.intersection(set7)
print(set8)
# you can also use the & for the same result but only for sets
#intersectio updat ereturns the original set
x = set1.intersection_update(set6)
print(x)
#The oppoiste is difference() which returns different items not duplicates
set9 = {"Goku", "Vegeta", "Kratos"}
l = set5.difference(set9)
print(l)
# The difference update() method keeps the items from the first set that are not in the other set but will change the original set.
thisset1 = {"England", "Scotland", "Ireland"}
thisset2 = {"Wales", "England", "Scotland"}
thisset1.difference_update(thisset2)
print(thisset1)
# Symmetric difference () will keep the the items that are not in both sets. or use the ^ operator
thisset3 = {"Samsung", "Apple", "Oppo"}
thisset4 = {"Apple", "Microsoft", "Sony"}
thisset3.symmetric_difference(thisset4)
print(thisset3)
# Then there is symmetric_difference_update() will keep all differences but return the original set not a new set.
