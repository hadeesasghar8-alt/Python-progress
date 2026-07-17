# A recursion happens when a fucntion calls itself. Menaing you can loopmthrough data to reach.
def MP(n):
    if n <= 0:
        print("MP is depleted!.")
    else:
        print(n)
        MP(n-1)
MP(5)
# A base case- a condition that stops recursion.
# a recursive case - The fucntion calling itself with a modifed argument
def factorial(n):
    if n == 0 or n == 1:
        return 1
    # recursive case
    else:
        return n * factorial(n - 1)
print(factorial(5))
# Fibonacci Sequence is a rule where the next number is the sum of the previous two
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(7))
# Can also use to process lists by handling one elemnet at the time:
def sum_list(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] + sum_list(numbers[1:])
My_list = [1 ,2, 3, 4, 5]
print(sum_list(My_list))
"""
YOU CAN UP THE DEAFULT LIMIT OF THE RECURSIVE CELLS
"""