x = 10  # Global

def outer():
    x = 5  # Enclosing
    def inner():
        x = 1  # Local
        print(x)
    print(x) # enclosing
    inner()
print(x) # global
outer()  # Output: 1

# To edit enclosing and global variables, use the nonlocal and global keywords respectively.

# enclosing example
def outer():
    x = 5
    def inner():
        nonlocal x
        x = 1
        print(x) #Local variable changed output 1
    print(x) #enclosing variable output 5 as inner is not called yet
    inner()
    print(x) #enclosed variable changed output 1

outer()

# global example
def outer():
    global x
    x = 5
    def inner():
        global x
        x = 1
        print(x) #global variable changed output 1
    print(x) #global variable output 5
    inner()
    print(x) #global variable changed output 1

print(x) #global variable output 10 as outer is not called yet
outer()