# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memeory location
"""
is  	Returns True if both variables are the same object 	    x is y 	
is not 	Returns True if both variables are not the same object 	x is not y
"""
x = ["apple", "Bannana"]
y = ["apple", "Bannana"]
z = x 
print( x is z)
print( x is not y)
print( x == y)
# The is not operator returns true if both variables do not point to the same object.
