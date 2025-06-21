a = [1,2,3]
b=a
b.append(4)

print('a,b')
print(a)
print(b)

# What is the output of the code above?
# They will both be [1,2,3,4]. 
# This is because lists are mutable objects, so when you assign a list to another variable, you are actually assigning a reference to the list. 
# Therefore, when you modify the list using one variable, the changes will be reflected in the other variable as well. 
# If you want to create a copy of the list, you can use the copy() method or the list() constructor.

a1 = [1,2,3]
b1 = a1.copy()
b1.append(4)

print('a1,b1')
print(a1)
print(b1)

# The output of the code above will be [1,2,3] and [1,2,3,4].
# This is because the copy() method creates a shallow copy of the list, which means that it creates a new list with the same elements as the original list.

# Because copy method only creates a shallow copy of the list, nested items will only have it's reference copied and not the actual item.

a2 = [1,2,3,[4,5,6]]
b2 = a2.copy()
b2[3].append(7)

print('a2,b2')
print(a2)
print(b2)

# The output of the code above will be [1,2,3,[4,5,6,7]] and [1,2,3,[4,5,6,7]].

# To create a deep copy of the list, you can use the deepcopy() function from the copy module.

import copy

a3 = [1,2,3,[4,5,6]]
b3 = copy.deepcopy(a3)
b3[3].append(7)

print('a3,b3')
print(a3)
print(b3)

# The output of the code above will be [1,2,3,[4,5,6]] and [1,2,3,[4,5,6,7]].

# List constructor can also be used to create a shallow copy of the list.

a4 = [1,2,3,[4,5,6]]
b4 = list(a4)
b4[3].append(7)

print('a4,b4')
print(a4)
print(b4)

# The output of the code above will be [1,2,3,[4,5,6,7]] and [1,2,3,[4,5,6,7]].