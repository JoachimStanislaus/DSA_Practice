# 443. String Compression

# Given an array of characters chars, compress it using the following algorithm:

# Begin with an empty string s. For each group of consecutive repeating characters in chars:

# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

# After you are done modifying the input array, return the new length of the array.

# You must write an algorithm that uses only constant extra space.

# Example 1:

# Input: chars = ["a","a","b","b","c","c","c"]
# Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
# Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
# Example 2:

# Input: chars = ["a"]
# Output: Return 1, and the first character of the input array should be: ["a"]
# Explanation: The only group is "a", which remains uncompressed since it's a single character.
# Example 3:

# Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
# Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".

# Constraints:

# 1 <= chars.length <= 2000
# chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        N = len(chars)
        write_pointer = 0
        read_pointer = 0

        current_character = None
        current_run = 0

        def write_buffer(write_pointer):

            if current_character is not None:
                chars[write_pointer] = current_character
                write_pointer+=1

                if current_run > 1:
                    for x in str(current_run):
                        chars[write_pointer] = x
                        write_pointer += 1
            return write_pointer

        while read_pointer < N:
            c = chars[read_pointer]
            read_pointer += 1

            if c == current_character:
                current_run += 1
            else:
                write_pointer = write_buffer(write_pointer)

                current_character = c
                current_run = 1
        
        write_pointer = write_buffer(write_pointer)

        return write_pointer