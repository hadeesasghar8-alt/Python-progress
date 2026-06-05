# The ternary operator allows you to assing one value if a condidtion is true and another if it is false.
num = 6
x = "Dante" if num > 5 else "Vergil"
print(x)
# The ternary operator is not an actual opertor it is a condidiotnal expression.
# and is used instead of elif in longer statments
num = 7
x = "Fri" if num == 5 else "sat" if num == 6 else "Sun" if num == 7 else "weekday"
print(x)