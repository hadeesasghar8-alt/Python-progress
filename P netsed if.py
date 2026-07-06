# you can nest if statments into if statments
x = 57
if x > 10:
    print("x is greater than 10")
    if x > 50:
        print("x is greater than 50")
# only runs if the first statement is true
# it works by making deeper levels of decision making
age = 18
has_righttovote = True
if age >= 18:
    if has_righttovote:
        print("You can vote")
    if age == 18:
        print("You are exactly 18 years old")
    else:
        print("You are too young to vote")
# multiple if statements above one printed string will print that one string if they are true
# you can nest as many as you want but to many will make code too hard to read
# as well as use logical operators to help simplify the code
Europe = True
is_France = True
if Europe and is_France:
    print("You are located in Paris")