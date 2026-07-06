# the else keyword catches anything not caught by the preceding conditions
# so executed whne if and elif are false
a = 50 
b = 400
if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
else:
    print("a is way less than b")
# you can also have else without elif
#note that else must come last in the code
# its acts as a fall back and a catch all fucntion for any scenraio within the code the reurn atleast one value
x = 6
y = 7
if x > y:
    print("x is greater than y")
elif x==y:
    print("x is equal to y")
elif x >= y:
    print("x is greater than or equal to y")
else:
    print("x is less than y")