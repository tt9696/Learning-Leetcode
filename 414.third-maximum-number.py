#
# @lc app=leetcode id=414 lang=python
#
# [414] Third Maximum Number
#

# @lc code=start
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first, second, third = None, None, None

        for num in nums:
            if num in (first, second, third):
                continue  # Ignore duplicates, skips duplicate number

            if first is None or num> first:
                first, second, third = num, first, second
            elif second is None or num > second:
                second, third = num, second
            elif third is None or num > third:
                third = num

        if third is None: # no 3rd maximum
            return first 
            
        return third

        
# @lc code=end

