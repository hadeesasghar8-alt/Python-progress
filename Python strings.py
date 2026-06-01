""""
Strings in Python are surrounded by single or double quotation marks
You can display a string literal with the print() func.
You can use quotes inside quotes as long as the quoataion marks differ between both.
"""
print("it's a string")
print('She is a string')
print('He is called "Dante"')
# You can assign a string to a variable and then use that variable to print the string
X = "bye"
print(X)
# Multiline strings can be denoted with three quotes, either single or double.
a = """This is a multiline string,
and it will be three lines long, 
because i can do it lol."""
print(a)
# Strings are arrays, which means you can access individual characters in a string by using an index
# Python does not have a built in charcter data typem a single charcter is a string of a length of 1.
b = "Hello, World"
print(b[0])
# As strings are arrays we can loop charcters through the string with a for loop.
for x in "Dante":
    print(x)
# This prints thew string in differnt lines.
for x in "Vergil":
    print(x)
    # the length of a string can be found with the len() function.
    print(len("Nero"))
# to check if a certain phrase or charcter is present in a string you can use the in keyword 
if "Dante" in "Dante is a charcter in Devil May Cry":
    print("Yes, 'Dante' is present.")
    # adversly to check if a phrase or charcter is not in a string you can use the not keyword.
    if "Vergil" not in "Dante is a chacrter in Devil May Cry":
        print("no, 'Vergil' is not present.")
    # You can also set a string as a txt varaible and then chechk for the string length.
    txt = "Liz loves cookie pies"
    print(txt)
    print(len(txt))
    print(txt[2])
    #note spaces count as chacrters in a string.