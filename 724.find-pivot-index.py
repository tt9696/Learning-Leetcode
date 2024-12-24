#
# @lc app=leetcode id=724 lang=python
#
# [724] Find Pivot Index
#

# @lc code=start
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = sum(nums)
        left_sum = 0
        right_sum = 0
        for i, num in enumerate(nums):
            right_sum = total_sum - left_sum - num
            if left_sum == right_sum:
                return i #index
            left_sum += num 

        return -1 # no index

        
# @lc code=end

