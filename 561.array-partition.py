#
# @lc app=leetcode id=561 lang=python
#
# [561] Array Partition
#

# @lc code=start
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # to maximize the sum of the minimum values from n pairs. 
        # Sorted: [1, 2, 2, 5, 6, 6] → Pairs: (1,2), (2,5), (6,6) 
        # min of 1 ,2, 6→ Sum: 1+2+6=9
        nums.sort()
        total_sum = 0
        for i in range(0, len(nums), 2):#Iterates through every second index:0 2 4
            total_sum += nums[i]
        return total_sum

        
# @lc code=end

"""
return sum(sorted(nums)[::2]) #[::2] picks every second element (i.e., the first element of each pair).
"""