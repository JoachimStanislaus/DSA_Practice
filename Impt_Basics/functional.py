# map
# Used to apply a function to each item in a iterable (like a list) and return a new iterable

numbers=[1,2,3,4,5]
result = map(lambda x: x * 2, numbers) # multiply each item in list by 2
print(list(result))


# filter
# Used to filter elements from an iterable based on a condition (function that returns True / False)

numbers = [1,2,3,4,5,6]
result = filter(lambda x: x%2 == 0, numbers) # Get even numbers from the list
print(list(result))

# reduce
# Used to apply a function cumulatively to the elements of an iterable reducing it to a single value.

from functools import reduce
numbers = [1,2,3,4]
result = reduce(lambda x, y: x*y, numbers) # Calculate product of all elements in a list
print(result)

# List Comprehensions
# Concise way to create lists in python
squares = [x ** 2 for x in range(5)]
print(squares)

numbers = [1,2,3,4,5,6]
evens = [x for x in numbers if x%2 ==0]
print(evens)

# product of two lists
result = [(x,y) for x in [1,2] for y in [3,4]]
print(result) # Output [(1, 3), (1, 4), (2, 3), (2, 4)]

# Generator Functions
# Generator functions use yield instead of return to produce values one at a time, pausing and resuming where it left off
# saves memory by not storing all values in memory at once
# Numbers are generated one at a time and not stored in memory unless converted to a list explicitly.

def my_generator(n):
    for i in range(n):
        yield i

gen = my_generator(5)

for value in gen:
    print(value)

# Generator Expressions
# Concise way to create generators, similar to list comprehensions, but using parentheses () instead of []
squares = (x **2 for x in range(5))
print(list(squares))