# OOP organises code into reusable objects

# Defining a class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi, my name is {self.name}.")

person1 = Person("Alice", 30)
person2 = Person("Bob",25)

print(person1.name)
person2.greet()

# Encapsulation restricts access to some of the object's components, bundling data (attributes) and the methods (functions) that operate on that data into a single unit.
# Direct access to the data is restricted, and access is provided only through methods (getters and setters).
# can use _ (protected) or __ (private) to control access.
class BankAccount:
    def __init__(self,balance,name):
        self.__balance = balance # (private) attribute
        self._name = name # (protected) attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
    
    def get_owner(self):
        return self._name

account = BankAccount(1000,"John")
account.deposit(500)
print(account.get_balance())
print(account.get_owner())
print(account._name) # Still able to access as not enforced to be strictly internal to the class (protected) attribute
# print(account.__balance) # Unable to access as (private) attribute is enforced to be strictly internal to the class

# Private is enforced while protected is not enforced

class Example:
    def __init__(self):
        self._protected_attribute="protected"
        self.__private_attribute='private'

class Subclass(Example):
    def access_protected(self):
        return self._protected_attribute
    
    def access_private(self):
        return self.__private_attribute
    
obj = Subclass()
print(obj.access_protected()) # Accessed through subclass
print(obj._protected_attribute)  # Can still be accessed, but discouraged

# print(obj.access_private()) # Unable to access through subclass as private attribute is enforced to be strictly internal to the class
# print(obj.__private_attribute) # Unable to access through subclass as private attribute is enforced to be strictly internal to the class

# Inheritance
# Inheritance allows a class to inherit attributes and methods from another class (parent class).

class Animal:
    def __init__(self,breed):
        self.__breed = breed

    def speak(self):
        print("I make a sound")
    
    def get_breed(self):
        return self.__breed
    
    def change_breed(self,breed):
        self.__breed = breed

class Dog(Animal):
    def speak(self): # overriding function
        super().speak() # super() calls the parent class method
        print("woof")


dog = Dog("dog")
dog.speak()
# Getter & Setter methods that work with private attributes can be inherited 
print(dog.get_breed())
dog.change_breed("cat")
print(dog.get_breed())


# Diamond Problem in Multiple Inheritance: 
# When multiple parent classes have a method with the same name, the method resolution order (MRO) determines which one is called.

class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        print("Hello from B")

class C(A):
    def greet(self):
        print("Hello from C")

class D(B, C):
    pass

obj = D()
obj.greet()  # Hello from B (MRO: D -> B -> C -> A)

# Accessing private attribute via name mangling
class Parent:
    def __init__(self):
        self.__attribute = "Parent's private attribute"

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__attribute = "Child's private attribute"  # Different from Parent's __attribute

obj = Child()
print(obj._Parent__attribute)  # Access Parent's private attribute
# print(obj.__attribute)  # Access Child's private attribute won't work
print(obj._Child__attribute) # Will work as using name mangling

# Polymorphism
# Allows different classes to be treated uniformly via shared methods

class Cat(Animal):
    def speak(self):
        print("Meow!")

animals = [Dog("dog"), Cat("cat")]
for animal in animals:
    animal.speak() # prints woof & meow


class Bird:
    def fly(self):
        print("Bird is flying")

class Airplane:
    def fly(self):
        print("Airplane is flying")

class Fish:
    def swim(self):
        print("Fish is swimming")

# Polymorphism through duck typing
for obj in [Bird(), Airplane(), Fish()]:
    if hasattr(obj, "fly"): # hasattr checks if attribute exists within the class, methods are considered an attribute of the class obj, pointing to a function obj.
        obj.fly()
    else:
        print("Object cannot fly")
# Output:
# Bird is flying
# Airplane is flying
# Object cannot fly


# Abstraction
# Hides the implementation details and shows only the essential features
# Any concrete subclass of an abstract class must implement all its abstract methods, or it will also remain abstract.
# You cannot create an object of an abstract class directly.
# Abstract classes serve as blueprints for designing frameworks or libraries.

from abc import ABC, abstractmethod

# Abstract Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# Subclass that implements the abstract methods
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
# Subclass that implements the abstract methods
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
    

shapes = [Rectangle(4,5), Circle(3)]
for shape in shapes:
    print(f"Area: {shape.area()}, Perimeter: {shape.perimeter()}")