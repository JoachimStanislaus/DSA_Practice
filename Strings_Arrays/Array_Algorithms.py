# 2. ARRAY ALGORITHMS
basicArray = [1,2,3,4,5]

# - Reverse an Array
print('Reverse an Array')
print('original array: ', basicArray)
print('\nmethod 1')
reversedArray = basicArray[::-1]
print(reversedArray)

print('\nmethod 2')
basicArray.reverse()
print(basicArray)


# - Find the Maximum and Minimum in an Array
print('\nFind the Maximum and Minimum in an Array')
basicArray.sort()
maxValue = basicArray[-1]
minValue = basicArray[0]
print('\nmethod 1')
print('min: ',minValue)
print('max: ',maxValue)

print('\nmethod 2')
print('min: ', min(basicArray))
print('max: ', max(basicArray))

print('\nmethod 3')
maxValue = 0
minValue = 99999999999999
for num in basicArray:
    if num < minValue:
        minValue = num
    if num > maxValue:
        maxValue = num
print('min:', minValue)
print('max:', maxValue)

# - Check for Duplicates
print('\nCheck for Duplicates')

print('\nNo Duplicates:')
print('original array: ',basicArray)
print(len(basicArray))
print(len(set(basicArray)))

basicArray.append(1)
print('array with duplicate', basicArray)
print(len(basicArray))
print(len(set(basicArray)))
if (len(basicArray) != len(set(basicArray))):
    print('there is a duplicate')

# How to identify duplicate?
print('\nHow to identify duplicate?')
# Method 1 (Sorting will use less memory but less efficient)
print('\nMethod 1')
basicArray.sort()
duplicateList = []
prevItem = None
for item in basicArray:
    if item == prevItem:
        duplicateList.append(item)
    prevItem = item

print('duplicates:', duplicateList)

# Method 2 (More efficient but more memory compared to method 1)
print('\nMethod 2') 
seen = set()
duplicate = set()

for i in basicArray:
    if i not in seen:
        seen.add(i)
    else:
        duplicate.add(i)

print('duplicates:', duplicate)

# - Rotate Array to the Right by K steps
print('\nRotate Array to the Right by K steps')
print('Original Array: ', basicArray)

def rotateRightByK(k):
    n = len(basicArray)
    k = k%n
    return basicArray[-k:] + basicArray[:-k]

print('Rotated Array',rotateRightByK(3))