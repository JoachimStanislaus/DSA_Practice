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
