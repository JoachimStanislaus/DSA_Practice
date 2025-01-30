# arg example where you expect a list of unnamed positional arguments.
def getarg(*args):
    # arguments are collected into a tuple for use inside the function
    print(args)

# kwarg example where you expect a set of named keyword arguments.
def getkwarg(**kwarg):
    # keyword arguments are collected into a dictionary for use inside the function
    for key, value in kwarg.items():
        print(f'{key}: {value}')
    

getkwarg(name='John', age=25, city='New York')
getarg(1,2,3,4,5)