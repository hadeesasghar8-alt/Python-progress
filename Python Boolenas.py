# Boolean values represent one of two values: true or false.
# In programming you often nheed to know if an expression is true or false.
# For example if you run am expression Python will give you the Boolean value.
print(10 > 9)
print(10 == 9)
print(10 < 9)
# You can also write expressions based on whether the statment is true or false.
a = 300
b = 4
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")        
"""
The bool() fucntion allows you to evaluate any value, and give you a true or false in return."""
print(bool("Hello"))
print(bool(15))
x = "Hello"
y = 15
print(bool(x))
print(bool(y))
"""
Most values are evaluated to be true if it has some content.
Any string is True except empty strings.
Any number is True except 0.
As well as any list, Tuple set and dictionary are true, except empty ones."""
bool("abc")
bool(567)
bool(["apple", "pear","banana"])
# Naturally there are less false values as most string or numbers contain a value. unlike empty functions. 
bool(False)
bool(None)
bool(0)
bool(())
#  Another vlaue that evaluates to false is an object made from a class with a __len__ function that returns 0 or False.
class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))
# Functions can als o return a Boolean
def myfunc1() :
    return True
print(myfunc1())
# You can also excute code basedd on the Boolean value given,
def myfunc2() :
    return True
if myfunc2():
    print("Yes")
else:
    print("No")
# P also has bulit in functions that return a boolean value such as isinstance() fucntion, which determines if an object is of a certain data type.
O = 67
print(isinstance(O, int))
