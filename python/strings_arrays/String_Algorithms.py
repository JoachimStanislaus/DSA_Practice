# - Count Occurrences of a Character
print('Count Occurrences of a Character')
testString = '123123'

def countChar(string,character):
    count = 0
    for x in string:
        if x == character:
            count+=1
    return count

print(countChar(testString,'1'))

# - Check Anagram (basically if the words use the same letters & number of letters)
print('\nCheck Anagram')

def checkAnagram(string1,string2):
    string1 = list(string1)
    string2 = list(string2)
    if (len(string1) == len(string2)):
        for x in string1:
            if x in string2:
                string2.remove(x)
        if len(string2) == 0:
            return True
        else:
            return False
    else:
        return False

print(checkAnagram('123','322'))


# - Find First Non-Repeating Character
print('\nFind First Non-Repeating Character')
# Method 1 O(n^2)
print('\nMethod 1')
def firstNonRepeatChar(string):
    string = list(string)
    
    for x in range(len(string)):
        poppedValue = string.pop()
        if poppedValue in string:
            string.remove(poppedValue)
        else:
            print('non repeat:',poppedValue)
            break

firstNonRepeatChar('1231234')

# Method 2 O(n)
print('\nMethod 2')
def firstNonRepChar(string):
    count_char={}
    for char in string:
        count_char[char] = count_char.get(char,0)+1

    for char in count_char:
        if count_char[char] == 1:
            print('char no repeat:', char)

firstNonRepChar('1231234')
