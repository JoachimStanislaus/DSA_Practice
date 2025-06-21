# single input lambda function
square= lambda x: x*x
print(square(5)) # Output: 25

# Lambda functions can take multiple arguments
sumarg= lambda x,y: x+y
print(sumarg(5,6)) # Output: 11

# Lambda functions can be used as an anonymous function inside another function
def myfunc(n):
  return lambda a: a*n

# Lambda can take in list as input
sumlist= lambda lst: sum(lst)
print(sumlist([1,2,3,4,5])) # Output: 15

# Lambda taking in multiple lists as input
sumMultiList= lambda lst1,lst2: sum(lst1) + sum(lst2)
print(sumMultiList([1,2,3],[4,5,6])) # Output: 21
