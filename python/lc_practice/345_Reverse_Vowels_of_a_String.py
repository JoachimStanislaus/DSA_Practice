# 345. Reverse Vowels of a String

# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# Example 1:

# Input: s = "IceCreAm"

# Output: "AceCreIm"

# Explanation:

# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:

# Input: s = "leetcode"

# Output: "leotcede"

# Constraints:

# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = list(s)
        vowelList = ['a','e','i','o','u','A','E','I','O','U']
        vowelsFound = []
        vowelIndex = []
        index = 0
        for letter in s:
            if letter in vowelList:
                vowelsFound.append(letter)
                vowelIndex.append(index)
            index+=1
        
        vowelsFound = vowelsFound[::-1]
        index = 0
        for Vindex in vowelIndex:
            res[Vindex] = vowelsFound[index]
            index+=1
        
        return ''.join(res)