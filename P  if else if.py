# Python supourts the usual logical condiitons from maths
"""
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
these are commonly used in condiotnal statements and loops
starts with an if keyword
"""
a = 50
b = 10
if a > b:
    print("a is greater than b")
"""
If statements evualute a condition that is either true or false, then if it is true exceutes that block and false skips it"""
x = -1
if x > 0:
    print("The number is a positive number")
    # False statment, so the code will not execute
# You can also do multiple statements in a single block, but must be indented the same amount.
time = 11.30
if time < 12.00:
    print("its the morning")
    print("its almost noon")
# Boolean variables can be used directly in if statements, as they are already true or false
is_snowing = True
if is_snowing:
    print("its winter")