#
# @lc app=leetcode id=283 lang=python
#
# [283] Move Zeroes
#

# @lc code=start
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0 :
                nums[i], nums[j] = nums[j] , nums[i]
                j += 1

# @lc code=end

"""
nums = [0, 1, 0, 3, 12]
if use pointer swap, result => nums = [12, 1, 3, 0, 0] 
[1, 3, 12] are no longer in their original order, output should be [1,3,12,0,0]

    nonZeroIndex = 0

    # Move all non-zero elements forward
    for i in range(len(nums)):
        if nums[i] != 0 :
            nums[nonZeroIndex] = nums[i] #  Place 1 at nums[0]
            nonZeroIndex += 1 

    # Fill the rest of the array with zeros
    # original nums = [0, 1, 0, 3, 12]        
    # nums = [1, 3, 12, 3, 12]
    # Starting from nonZeroIndex = 3 to the end, fill with zeros:
    # nums[3] = 0, nums[4] = 0 → nums = [1, 3, 12, 0, 0]
    for i in range(nonZeroIndex, len(nums)):
        nums[i] = 0
"""