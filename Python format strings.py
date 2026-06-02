# you cannot cobine strings and nubers using the + operator
# Eg. age = 25
# txt = "My name is Goofy and I am " + age
# print(txt)
# This will produce an error beacuse age is a number and txt is a string.
# To fix this we can use f-strings to format() the string.
age = 25
txt = f"My name is Donald and I am {age} years old."
print(txt)
# So you put the f infront of a string literal and then use curly brackets to include the variable you want to insert into the string.
# the curly brakctes are placeholders for the variable and other operations.
# Place holders can contain variables, opertaions, fucntions and modifers to format the value.
price = 67.99
txt = f"The price of the game is {price} pounds"
print(txt)
# using .2f will format the number to 2 decimal places.
txt = f"The price of the game is {price:.2f} pounds"
print(txt)
# the modifier is the :
txt = f"The price of the game is {price:10.2f} pounds"
print(txt)
# The placeholder can contain maths operations.
txt = f"The price of Devil May Cry 5 on release was {10*5} pounds"
print(txt)
# You can also use the format() method to format strings.
txt = "The price of the game is {} pounds".format(price)        
print(txt)  