# Explain what OOP is in your own words
# OOP stands for object oriented programming, it helps improve maintainability, code reuse, readability, flexibility. Key concepts consists of Inheritance, Encapsulation, Abstraction, Polymorphism.

# Explain the 4 concepts of OOP, Inheritance, Encapsulation, Abstraction, Polymorphism

# Inheritance - when we have a parent class and a child class, Animal parent class and maybe dog and cat child classes. 
# We can put shared attributes and methods in the parent class which can be inherited and used in child classes promoting code reuse.

# Encapsulation - Restricts access to attributes, we have private and protected attributes for python, 
# protected is not enforced and is more of a notice / reminder whilst private is enforced but can be overcome using name mangling but we should only use it for testing/debugging.

# Abstraction - Abstraction would be like providing a template like structure, if we use it methods in the parent class that are abstract must exist in the child class, 
# it also hides the implementation of methods by leaving the details to be implemented in the subclasses.

# Polymorphism - would be many different child classes of the same parent class each having the same method but each performing something different. 
# It allows methods with the same name to behave differently depending on the object that invokes it.

# Explain what Multithreading and Multiprocessing is?
# Multithreading - Imagine a complex math problem, we can split it up into smaller problems for 1 person to multi-task and resolve. (shared memory and resource) (threads run within same process)
# Multiprocessing - Imagine a complex math problem as well, but this time we can split it into smaller problems for multiple people to resolve. (Not shared memory) (Multiple processes as name suggests)

# Explain what Async and Synchronous is
# Async would be a chef cooking in the kitchen and a waiter, whilst the chef is cooking the waiter can continue doing other tasks until the food is cooked to go back and collect it.
# Essentially waiting for the task to complete and doing something else in the meantime.

# Synchrous would be tasks executed in sequential order where we have to complete each task to start on the next one.

# Explain what class and static class methods are
# Class methods allow the manipulation and access of class attributes whilst static class methods are used for utility/helper methods and cannot access instance or class attributes.

# Does python pass by reference or value?
# Python uses pass-by-object-reference, always passes the reference to the object, not the actual value of the object or a copy.
# Whether the behavior appears to be "pass by reference" or "pass by value" depends on the mutability of the object being passed.
# It depends on whether the type is immutable or mutable. Mutable types pass by reference whilst immutable pass by value.

# How do you make a copy of a List?
# Make a deepcopy by importing copy
# shallow copy of the list will still only reference nested lists.

# What are comprehensions in python.
# Comprehensions are a concise way to create new sequences like lists, sets, dictionaries etc.
# Makes code shorter, more readable and more efficient.
# eg. [x for x in [1,2,3] if x == 1]

# Are comprehensions faster than for loops? Why?
# Comprehensions are faster than for loops as When you use a for loop, on every iteration, you have to look up the variable holding the list and then call its append() function. 
# This doesn't happen in a list comprehension. Instead, there is a special bytecode instruction LIST_APPEND that will append the current value to the list you're constructing.

# What are generators and can you describe how generator really work?
# They are iterators that allow you to product a sequence of values lazily (one at a time, only when needed) instead of creating the whole sequence in memory at once.
# Memory efficient and great for working with large or infinite sequences
# squares = (x**2 for x in range(5))
# print(next(squares))  # 0
# print(next(squares))  # 1
# Each call to next() runs the function until the next yield, then pauses.

# Mutable and Non-Mutable data types.
# Mutable: List, Dictionary, Set
# Immutable: Integer, Float, String, Tuple, frozenset
# tuples are immutable but it can hold mutable objects
# immutable objects that are literals(written specifically not dynamically created during runtime) are interned (reused)

# Small integers (usually from -5 to 256) are automatically interned(reused).
# These integers are created at compile-time as literals.
# Larger integers (outside -5 to 256) are not automatically interned.
# Python creates a new object each time the literal is used at runtime.

# Is set mutable?
# Yes

# What is the difference between is and =
# I=is compares the actual object while = compares the value

# What are Lambda Functions?
# They are short concise anonymous functions that are usually one liners but you can assign it to a variable.

# Method Overloading. Does Python support Method overloading?
# No
