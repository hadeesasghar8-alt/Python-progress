x = "Dante"
def myfunc():
    print("Vergil" + x)   
  # Variables created outside the def myfunc() fucntion are known as global variables and can be used inside and outside funtions.
def myfunc2():
    x = "Nero"
    print("Vergil" + x) 
    return x   
# You can print a function inside a function to stop the line from printing many times, instead use the return function to return to the main code and print the result there.
# If you create a variable with the same name inside a function, this variable will be local and can only be used inside the function. The global variable with the same name will remain unchanged.
# Also after researching online always end a function with a return statement to avoid errors and to make the code more efficient and printing functions is not recommended if you are expecting a result back not like a damage number in game but if its just for text then no need to return a value.
# Also i can create a global variable inside a function by using the global keyword.
def func3():
    global x
    x = "PO"
   
    myfunc()
    result = myfunc2()
func3()
print("The dragon warrior is " + x)