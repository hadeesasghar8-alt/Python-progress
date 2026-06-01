"""
When specifing a variable, using construcor fucntions can help.
useing the str(), int() and float() fucntions
these will convert whatever value in thats specific variable type
eg if x = 5, then str(x) would be 5 but float(X) would be 5.0.
"""
x = int(5) 
y = int(6.6)
z = int("7")
print(x)
print(y)        
print(z)
# note you cannot convert a string into an integer if does not have a number in it, or if it has a decimal point.
w = float(5)
v = float(6.6)
u = float("7")
f = float("7.5")
print(w)
print(v)        
print(u)
print(f)
i = str("s1")
l = str(5)
b = str(7.6)
print(i)
print(l)    
print(b)