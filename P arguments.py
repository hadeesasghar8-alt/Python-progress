# info can be passed as arguments.
"""
Arguments are specifed after the function made insde the parentheses"""
def characters(fname):
    print(fname + " DMC")
characters("Dante")
characters("Vergil")
characters("Nero")
# a parameter is the variable listed inside the brackets in the function creation block, whereas an arguemnt is the value sent to the fucntion when it is called.
"""For example
def character(name):  name is the parameter
     print("Hello" , name)
character("Dante) is an argument"""
# If the funtion expects 2 arguments and only one is presented it will not be executed.
# You can assging default values to parameters.
def characters(Name = "Side Character"):
    print("Bleach", Name)
characters("Ichigo")
characters("Rukia")
characters()
# There are also Key word arguments key = value syntax
def Spells(Element, name):
    print("Cast", name)
    print("My spell is called", name, "and is the element of", Element)
Spells(Element = "FIRE", name = "Pyro")
# The order of arguments does not matter.
# If you call a fucntion without arguemtns its called a postional arguemtns and it the arguemtns must be in the right order.
def Terrain(Biome, name):
    print("I am in the", name)
    print("I am in the", name, "Which is the", Biome, "Biome")
Terrain("Tundra", "North Pole")
# You cna mix both positonal and key word arguemnts but the postinal arguemnts must come first
def C(Characters):
    for Character in Characters:
        print(Character)
my_characters = {"Dante", "Vergil", "Nero"}
C(my_characters)
def func1(x, y):
    return x + y
result = func1(5, 6)
print(result)
# You can specify that a fucntion has only one positional argument with(,/) AFTER THE ARGUMENT
# Key word only agruemtns use (*) BEFORE THE ARGUEMNTS