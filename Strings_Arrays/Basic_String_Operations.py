# Basic String Operations
basicString = '12 3'
print('Original String:',basicString)


# - Accessing characters
print('\nAccessing characters')
print('accessing char:', basicString[1])

# - String Length
print('\nString Length')
print('string length: ',len(basicString))

# - Substrings
print('\nSubstrings')
print('substrings: ',basicString[0:2])

# - Concatenation
print('\nConcatenation')
additionalString = '456'
print(basicString+additionalString)

# - Reverse a String
print('\nReverse a String')
print(basicString[::-1])

# - Split and Join
print('\nSplit and Join')
splitString = basicString.split()

print('split String: ',splitString)
newString = ''

print('join String', newString.join(splitString))

# - Check Palindrome (A palindrome is a word, phrase, number, or sequence that reads the same backward as forward (ignoring spaces, punctuation, and capitalization).)
print('\nqCheck if Palindrome')
palindrome = 'rotor'

if (palindrome == palindrome[::-1]):
    print('palindrome!')