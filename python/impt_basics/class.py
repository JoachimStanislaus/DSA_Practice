class Animal(object):
    count=1

    def get_count(self):
        return self.count
    
    @classmethod # Class methods have access to class variables and can be called without creating an object. They are used for factory methods. Factory methods are used to create an object of a class or subclass.
    def inc_count(cls): # cls is used to access class variables, while self is used to access instance variables.
        # A class method is a method that is bound to the class and not the instance of the class.
        # It can access and modify class-level attributes (shared across all instances). but not instance-specific data
        cls.count+=1
        return cls()

    @staticmethod # Static methods do not have access to class variables, but can be called without creating an object and are used for utility functions.
    # A static method is a method that belongs to the class but does not have access to the class (cls) or instance (self). It cannot modify or access class-level or instance-level data.
    def get_type():
        return "Animal"

class Dog():
    count = 1

    def get_count(self):
        return self.count

    def get_type(self):
        return "Dog"
    
test = Animal()
print(test.get_count())
Animal.inc_count()
print(test.get_count())