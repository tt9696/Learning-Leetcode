#
# @lc app=leetcode id=674 lang=python
#
# [674] Longest Continuous Increasing Subsequence
#

# @lc code=start
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        max_length = 1
        current_length = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                current_length += 1
                max_length = max(current_length, max_length)
            else:
                current_length = 1 # reset the length
        return max_length

# @lc code=end

