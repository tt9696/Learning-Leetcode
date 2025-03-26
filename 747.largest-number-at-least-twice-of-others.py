#
# @lc app=leetcode id=747 lang=python
#
# [747] Largest Number At Least Twice of Others
#

# @lc code=start
class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_index = 0

        for i in range(len(nums)):
            if nums[i] > nums[max_index]:
                max_index = i # index of max num
            
        for i in range(len(nums)):
            twice_num = 2 * nums[i]
            if i != max_index and nums[max_index] < twice_num:# whether the largest number is at least twice as large 
                return -1
        
        return max_index
        
# @lc code=end
"""
    max_index = 0
    second_large = float('-inf')# A very small number

    for i in range(1,len(nums)):
        if nums[i] > nums[max_index]:
            second_large = nums[max_index]
            max_index = i # index of max num
        elif nums[i] > second_large:
            second_large = nums[i]
    
    # Check if the max number is at least twice as large as the second max
    # If it is twice as large as the second largest number, it is automatically twice as large as all smaller numbers too.
    if nums[max_index] >= 2* second_max:
        return max_index
    return -1
"""
