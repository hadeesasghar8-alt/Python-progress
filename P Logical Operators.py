# Logical operators are used to combine conditional statments.
"""      
and  	Returns True if both statements are true 	                x < 5 and  x < 10 	
or 	    Returns True if one of the statements is true 	            x < 5 or x < 4 	
not 	Reverse the result, returns False if the result is true 	not(x < 5 and x < 10)
"""
x = 5
print(x > 0 and x < 10)
m = 5
print(m < 5 or m > 10)
print(not(m == 5 and m < 4))