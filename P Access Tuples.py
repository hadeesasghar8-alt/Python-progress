# You can access tuple item by refering to the index numbers
thistuple = ("apple", "Bananna", "Pear")
print(thistuple[0])
#Negative indexing refers to start from the end -1 is the last item and -2 is the second to last item.
print(thistuple[-1])
# You can also specify a rnage of indexes to be shown 
#When specifying the return value will be a new tuple
# If the index is [2:5] the search will start at 2 and at index 5 BUT NOT INCLUDE 5 
newtuple = ("Dante", "Vergil", "Nero", "Lady", "Trish", "V", "Mundus", "Sparda", "Mary")
print(newtuple[2:5])
#EXactly DID NOT INCLUDE V WHICH IS INDEX 5
#Now if you leave out the end index the search will go to the end
print(newtuple[2:])
#You can also range negative indexes
print(newtuple[-4:-1])
