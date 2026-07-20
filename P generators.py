# Generators are fucntions that can pause and resime their execution.
#they return generator objects, which is an iterator.
# The code is complied not executed until it is iterated over the genrator.
def ManaPoints():
    yield 1
    yield 2
    yield 3
    yield 4 
for value in ManaPoints():
    print(value)
# They allow you to iterate a dataset without stroing the entierty of it.
#It uses the yield keyword
#The yeild saves the fucntion state and is executed later when it is called upon
def MP(n):
    count = 1
    while count <= n:
        yield count
        count *=2
for ManaPoints in MP(10):
    print(ManaPoints)
#unlike like return that eliminates the fucntion yeild pauses it
#Gens save memory because they generate on executioin instad of storing it. Thus for large data sets its quite efficent
def NHS_Paitents(n):
    for i in range(n):
        yield i 
Appoitments = NHS_Paitents(10000)
print(next(Appoitments))
print(next(Appoitments))
print(next(Appoitments))
# using next pritns the next iterable 
# Similar to lists you can use genrators expressions
list_comp = [x * x for x in range(5)]
print(list_comp)
gen_exp = (x + 1 for x in range(900))
print(gen_exp)
print(list(gen_exp))
# can also be used to creat a fibannoci sequence
# Genrators the send(0 mehtod which allows you ti send a value to the gen
def echo_gen():
    while True:
        received = yield 
        print("Received:", received)
gen = echo_gen()
next(gen)
gen.send("Hello")
gen.send("World")
# stop() stops the generator
def ManaPoints():
    try:
        yield 1
        yield 2
        yield 3
        yield 4
    finally:
        print("Mana depleted")

gen = ManaPoints()
print(next(gen))
gen.close()

