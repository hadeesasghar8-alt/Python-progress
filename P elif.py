# The elif keyword is Python's way of saying if the previous condition is not true, try this new condition
a = 50
b = 10
if a < b:
    print("a is less than b")
elif a != b:
    print("a is not equal to b")
# you can do as many statments as you want not that it will stop at the first true statment, so multiple true statmens will not be executed.
# its use case is if you have mutally exclusive conditions to check, its more efficent than using if.