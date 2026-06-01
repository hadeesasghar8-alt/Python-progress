x = 5
y = 5.5
z = 1j
print(type(x))
print(type(y))
print(type(z))
# int is an integer, a whole number
# float is a decimal number
# complex is a number wiht a real number and an imaginary one.
# float can also use scientific nottaion wiht an "e" to indicat eto the power of ten
a= 67e6
print(a)
l = 1j
p = -5j
print(l)
print(p)
# you can also convert variable types with the int(), float() and complex() methods
t = 1
h = 22.5
c = 1j
n = float(t)
k = int(h)
m = complex(c)
print(n)
print(k)
print(m)
print(type(n))
print(type(k))
print(type(m))
# note you cannot convert complex numbers into different numeric types.
# P does not have a random number generator, but you can import the random module to do this.
import random
print(random.randrange(1,1000))
