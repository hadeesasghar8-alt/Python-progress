# Operator precedence desribes the order the operations are peformed.
"""
() 	Parentheses 	
** 	Exponentiation 	
+x  -x  ~x 	Unary plus, unary minus, and bitwise NOT 	
*  /  //  % 	Multiplication, division, floor division, and modulus 	
+  - 	Addition and subtraction 	
<<  >> 	Bitwise left and right shifts 	
& 	Bitwise AND 	
^ 	Bitwise XOR 	
| 	Bitwise OR 	
==  !=  >  >=  <  <=  is  is not  in  not in  	Comparisons, identity, and membership operators 	
not 	Logical NOT 	
and 	AND 	
or 	OR 	
"""
# If two operations have the same precedence they will be evaluated left to right instead.
print(5 + 7 - 3 + 6)
