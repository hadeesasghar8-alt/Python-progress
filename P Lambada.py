# A Lambada fucntion is a asmall anonmysous function. it can take any number od arguments but only give on expression.
Mp = lambda x : x + 10
print(Mp(5))
# it can take mulitple arguements
Mp = lambda x, y : x - y
print(Mp(5, 9))
# Lambda are commonly used in with other bulti in fucntion such as map(), filter(), and sorted()
Spells = [1 , 2 ,3 ,4 , 5]
doubled = list(map(lambda x : x *2, Spells))
print(doubled)
Spells = ["1", "2", "3"]
Casted_spell = list(filter(lambda x: x * 2, Spells))
print(Casted_spell)
Spells = [ ("Fire, 1"), ("Ice, 2"), ("Earth, 3")]
Casted_spell = sorted(Spells, key=lambda x: Spells[1])
print(Casted_spell)