# When a tupleis created we assing values to it which is called packing 
#But in Python we can extract the values back into vaiables which is calld unpacking 
fruits = ("apple", "pear", "orange")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red) 
# the number of variables must match the number of values in the tuple, if not you must add an * to collect the remaining values as a list
fruits = ("apple", "Banana", "Kiwi", "Dragon fruit")
(purple, black, *white) = fruits#
print(purple)
print(black)
print(white)
# I f the asterisk is another variabel that snot the last Python will assing variables until the number of values left matches the munber of variables left
Characters = ("Dante", "Vergil", "Nero", "Trish", "Lady", "V")
(green, *purple, red) = Characters
print(purple)
print(green)
print(red)
