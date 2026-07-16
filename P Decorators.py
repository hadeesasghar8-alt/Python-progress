# Decorators allow you to add extra behaviours to a fucntion. withiyt changeing the code
# A decorators is a fucntion that takes another fucntion as an input and returns a new fucntion.
def Spells(func):
    def ManaPoints():
        return func().upper()
    return ManaPoints
@Spells # This is the decorator
def Pyro(): # This is the function getting decorated
    return "Cast Pyro"
print(Pyro())
# You can call a decorator multiple times 
def Spells(fucn):
    def ManaPoints():
        return fucn().upper()
    return ManaPoints
@Spells
def Earth():
    return "Cast Quake"
@Spells
def Water():
    return "Cast Flood"
print(Water())
print(Earth())
# You can add arguments to decorators and *args and **kwargs
def Spells(func):
    def ManaPoints(*args):
     return func(*args).upper()
    return ManaPoints
@Spells
def Earth(name):
    return "Cast " +  name
print(Earth("Tremmor"))
def Spells(MP_cost):
    def decorator(func):

     def ManaPoints(*args):
         current_MP= 5

         if current_MP >= MP_cost:
             return "You have enough MP to cast" +func(*args)
         else:
             return  "You have an insuuficent amount of MP to cast." + func(*args)
        
     return ManaPoints
    return decorator
@Spells(5)
def Earth(name):
    return name
print(Earth(" Wall"))
# Functions in Python have meta data that can be returned with the _name_ attribute and _doc_.
def attacks():
    return "Light Punch, Heavy Punch, Medium Kick"
print(attacks.__name__)
# However when a fucntion is decorated the oringal data is lost
import functools
def Attacks(button_presses):
  def decorator(func):
      @ functools.wraps(func)
      def input(*args, **kwargs):
       Light = 1
       medium = 2
       Heavy = 3
       if button_presses == Light:
         return "Light button Combo" + func(*args, **kwargs).upper()
       else:
         return "Medium button combo" + func(*args, **kwargs).upper()
      return input
  return decorator

@Attacks(1)
def Combo():
   return " punch kick"
print(Combo())
