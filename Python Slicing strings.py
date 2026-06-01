# You can return a slice of charcters using the slice syntax.
#by the way a syntax is a set of rules that defines how a promgamming languages works.
x = "Gojo Sensei is weaker than Goku"#
print(x[0:5])
# The first chacrter has the index 0 and the second is 1 and so on.
# by leaving out the start index, the slice will start aty the frist charcter.
print(x[:2])
# Therefore the opposite stops at the set index and leaves ou t the restof the string.
print(x[7:])
# you can also negative indexes to start the slice from the end of the string.
print(x[-5:-2])