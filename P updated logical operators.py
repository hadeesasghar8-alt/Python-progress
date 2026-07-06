"""
Condition 1 	Condition 2 	            Result     for and operator
True 	           True 	                True
True 	           False 	                False
False 	           True 	                False
False 	           False 	                False """
""" 
Condition 1 	Condition 2 	        Result for or
True 	          True 	                True
True 	             False 	            True
False 	           True 	            True
False 	           False 	            False
"""
# for the rsult to be true for the and operator both conditions must be true
# whereas the or operator only condition needs to be true to return true.
# when using multiple operators use brackets to control and make the code readable
temp = 35
is_sunny = True
is_raining = False
if (temp > 30 and not is_raining) or is_sunny:
    print("its too hot today")