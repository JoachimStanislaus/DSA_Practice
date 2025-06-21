# 238. Product of Array Except Self

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

class Solution(object):

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        prefix = [1] * n
        postfix = [1] * n
        
        for index in range(len(nums)):
            if index == 0:
                prefix[index] = (nums[index])
            else:
                prefix[index] = (nums[index]*prefix[index-1])
        
        nums = nums[::-1]
        for index in range(len(nums)):
            if index == 0:
                postfix[index] = (nums[index])
            else:
                postfix[index] = (nums[index]*postfix[index-1])
        postfix = postfix[::-1]
        nums = nums[::-1]
        res = []
        for index in range(len(nums)):
            if index == 0:
                res.append(postfix[index+1])
            elif index == len(nums)-1:
                res.append(prefix[index-1])
            else:
                res.append(prefix[index-1]*postfix[index+1])
        return res