class Animal(object):
    count=1

    def get_count(self):
        return self.count
    
    @classmethod # Class methods have access to class variables and can be called without creating an object. They are used for factory methods. Factory methods are used to create an object of a class or subclass.
    def inc_count(cls): # cls is used to access class variables, while self is used to access instance variables.
        cls.count+=1
        return cls()

    @staticmethod # Static methods do not have access to class variables, but can be called without creating an object and are used for utility functions.
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