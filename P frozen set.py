"""
A frozen set is an immutable version of a set meaning you cannot add or remove elements
BUt still suppourts all non-mutating sets operations
copy() 	  	Returns a shallow copy 	
difference() 	- 	Returns a new frozenset with the difference 	
intersection() 	& 	Returns a new frozenset with the intersection 	
isdisjoint() 	  	Returns True if there is NO intersection between two frozensets 	
issubset() 	<= / < 	Returns True if this frozenset is a (proper) subset of another 	
issuperset() 	>= / > 	Returns True if this frozenset is a (proper) superset of another 	
symmetric_difference() 	^ 	Returns a new frozenset with the symmetric differences 	
union() 	| 	Returns a new frozenset containing the union"""
x = frozenset({"Dante", "Nero", "Vergil"})
print(x)
print(type(x)) 
