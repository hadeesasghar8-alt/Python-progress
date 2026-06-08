# You cna loop through the tuple items by usinf a for loop
thistuple = ("Apple", "Pear", "Kiwi")
for x in thistuple:
    print(x)
# You can also loop through tuple item using their index number 
for i in range(len(thistuple)):
    print(thistuple[i])
# You can also use a while loop  by using the len() function to detrmine the length of th etuple, then start at 0 and loop your way through the tuple items by refering to their indexes.
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1