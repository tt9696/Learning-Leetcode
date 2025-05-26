#
# @lc app=leetcode id=2148 lang=python
#
# [2148] Count Elements With Strictly Smaller and Greater Elements 
#

# @lc code=start
class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        min_val = min(nums)
        max_val = max(nums)

        for n in nums:
            if n > min_val and n < max_val: # if min_val < n < max_val:
                count += 1
        return count
        
# @lc code=end

