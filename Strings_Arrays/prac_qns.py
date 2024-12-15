# 5. PRACTICE QUESTIONS

# 1. Reverse a String without using slicing
print('Reverse a String without using slicing')

sampleString = '123123'

def reverseString(string):
    string = list(string)
    newlist = []
    for x in range(len(string)):
        poppedValue = string.pop()
        newlist.append(poppedValue)
    
    newstring = ''.join(newlist)
    return newstring

print(reverseString('123123'))
    
# 2. Find the Second Largest Element in an Array
print('\nFind the Second Largest Element in an Array')

# Method 1
print('\nMethod 1')

def findSecLargest(array1):
    array1.sort()
    return array1[-2]

print(findSecLargest([1,2,3,4,5]))

# Method 2
print('\nMethod 2')

def findSecoLargest(array1):
    biggestvalue = 0
    secondBigValue = 0
    for x in array1:
        if x > biggestvalue:
            secondBigValue = biggestvalue
            biggestvalue = x
    return secondBigValue

print(findSecoLargest([1,2,3,4,5]))

# 3. Check if a String Contains Only Digits
print('\nCheck if a String Contains Only Digits')

def onlyDigits(string):
    try: 
        string = int(string)
        return True
    except:
        return False
    
print(onlyDigits('12312a'))

# 4. Implement a Function to Rotate an Array Left by K Steps
print('\nImplement a Function to Rotate an Array Left by K Steps')

def rotateArray(array,k):
    return array[-k:] + array[:k]

print(rotateArray([1,2,3,4,5,6],3))

# 5. Longest Substring Without Repeating Characters

def longestSubstring(string):
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(string)):
        while string[right] in char_set:
            char_set.remove(string[left])
            left+=1

        char_set.add(string[right])

        if (max_length < right-left+1):
            max_length = right-left+1
    return max_length

print(longestSubstring('abcabcdefg'))