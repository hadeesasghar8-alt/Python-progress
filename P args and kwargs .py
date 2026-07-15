"""
by default a function must be called with the correct number of arguemnts
However sometimes the number of arguemnts may be unkown so using bot args and kwargs can accept the unkown number of arguments."""
def Spells(*Fire):
    print("Cast", Fire[2])
Spells("Pyro", "Inferno", "Blast")
# args allow a fucntion to accept any number of positional arguments, inside the fucntion argsd becaomes a tuple contiaing all  the passed argumemnts.
# combine them with regular parameters
def Spells(cast, *Water):
    for water in Water:
        print("cast", water)
Spells("Hydro", "Jet stream", "Flood")
"""
If you dont knwo how many keyword arguemnts will be passed add two ** before the parameter name
That it will reveive a dcitionary of arguments can access items properly"""
def Spells(**Earth):
    print("Cast", Earth["E1"])
Spells(E1 = "Quake", E2 = "Rock Shower")
# the ** Kwargs parameter  allows a fucntion to accept any number of keyword arguments, they become a dictionary of all those arguments.
# Like arhs Kwargs can be used alongside regular parameters.
def Spells(**Physco):
    for key in Physco:
        print("Cast")
        print(Physco[key])
Spells( cast1 = "Mass Hysteria", cast2 = "Physconic break")
# DONT MISS THE (KEY) PARAMETER 
# You can also cmobine both args and kwwargs
def Spells(MP, *Ice, **Dark):
    for key in Dark:
        print("Cast", Dark[key])
    else:
        for ice in Ice:
            print("Cast", ice)
Spells("Freeze", "Blizzard", cast2 = "Shroud", cast4 = "Expel light")
# The first word in the spells is the cast parameter the postional one
#You can use args and kwargs to unpack arguemnts.
def spells(pyro, water, ice):
    return "Pyro" + " Flood" + " Freeze"
Elements = ["fire", "water", "ice"]
result = spells(*Elements)
print(result)
