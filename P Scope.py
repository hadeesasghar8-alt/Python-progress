# A varibale is only available inside the range it is created. This is called a Scope
# Thus a Local scope means that variable made inside that scope can only be used inside that Scope.#
def ManaPoints():
    MP = 100
    print(MP)
ManaPoints()
# print(MP) tHIS wont work outside the fucntion beacvsue MP is tied to that scope.
# but it is available to fucntions insde the functions.
def ManaPoints():
   MP = 100
   def Mana_Usage():
     print(MP - 50)
   Mana_Usage() 
ManaPoints()
# In contrast Global Scope is any variable made outisde a fucntion
x = 60
def ManaPoints():
   MP = 100
   print(MP - x)
ManaPoints()
print(x)
# If you name Varibels with the same name but one is inside the fucntion and one is outisde they it can be executed.
MP = 500
def ManaPoints():
   MP = 100
   print(MP * MP)
ManaPoints()
# If you use the global key word you can bring a varibale out of its scope
def Super_Meter():
   global SP 
   SP = 100
Super_Meter()
print(SP)
# using global you can also change the value of an already existing global variable inside a scope
# you can only use the nonlocal keyword inside fucntion to push vairbales into the global scale
def Super_Meter():
   SP = 100
   print("Super is full")
   def Super_Meter_Empty():
      nonlocal SP 
      SP = 0
      Super_Meter()
      return SP
print(Super_Meter())

"""
Python uses these rules and searches for them in that order
Local - Inside the current function
Enclosing - Inside enclosing functions (from inner to outer)
Global - At the top level of the module
Built-in - In Python's built-in namespace
"""