# Basic Array Operations
basicArray = [1,2,3,4,5]

# - Accessing elements
print(basicArray[1])

# - Adding elements (append, insert)
basicArray.append(6)
print(basicArray)

basicArray.insert(3,4)
print(basicArray)

# - Removing elements (pop, remove)
lastitem = basicArray.pop()
print(basicArray)
print(lastitem)

basicArray.remove(4)
print(basicArray)

# - Iterating through an array
for i in basicArray:
    print(i)

