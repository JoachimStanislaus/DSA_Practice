# 1493. Longest Subarray of 1's After Deleting One Element

# Given a binary array nums, you should delete one element from it.

# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

# Example 1:

# Input: nums = [1,1,0,1]
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
# Example 2:

# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 5
# Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
# Example 3:

# Input: nums = [1,1,1]
# Output: 2
# Explanation: You must delete one element.
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.

class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        L=0
        R=0
        zerocount=0
        res = 0
        currentcount = 0

        for x in nums:
            if x == 0:
                if zerocount==0:
                    zerocount+=1
                    R+=1
                    currentcount+=1
                else:
                    while nums[L] != 0:
                        L+=1
                        currentcount-=1
                    L+=1
                    R+=1
            if x == 1:
                R+=1
                currentcount+=1
            if currentcount>res:
                res=currentcount
        return res-1
                