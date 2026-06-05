# Assignment opertoars assing values to variables
"""= 	x = 5 	x = 5 	
+= 	x += 3 	x = x + 3 	
-= 	x -= 3 	x = x - 3 	
*= 	x *= 3 	x = x * 3 	
/= 	x /= 3 	x = x / 3 	
%= 	x %= 3 	x = x % 3 	
//= 	x //= 3 	x = x // 3 	
**= 	x **= 3 	x = x ** 3 	
&= 	x &= 3 	x = x & 3 	
|= 	x |= 3 	x = x | 3 	
^= 	x ^= 3 	x = x ^ 3 	
>>= 	x >>= 3 	x = x >> 3 	
<<= 	x <<= 3 	x = x << 3 	
:= 	print(x := 3) 	x = 3"""
# The walrus operator := assinges values to variables as part of a larger expression
numbers = [1, 2, 3, 4,5]
if (count := len(numbers)) > 3:
    print(f"List the {count} elements")


print(x := 3)
x <<= 3
print(x)
