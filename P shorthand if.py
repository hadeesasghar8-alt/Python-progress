# if you have only one statment you can put in the same line
a = 5
b = 4
if a < b: print("a is less than b")
# the same with else
x = 6
y = 7
print("x is bigger than y") if x > y else print("y is bigger than x")
# This is known as a conditional expression or ternary operator
# You can also assing a value amd assing it to a variable
a = 7
b = 8
morethan = a if a > b else b
print("less than", morethan)
# you can do multiple conditons on the same line
# The condition and actions are simple
"""It improves code readability
You want to make a quick assignment based on a condition"""