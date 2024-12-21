#
# @lc app=leetcode id=334 lang=python
#
# [334] Increasing Triplet Subsequence
#

# @lc code=start
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = float('inf')
        second = float('inf')

        for num in nums :
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False

# @lc code=end
"""
For nums = [1, 2, 3, 4, 5]:
first = inf, second = inf
Iterating through the array:
For 1: first = 1, second = inf
For 2: first = 1, second = 2
For 3: Since 3 > 1 and 3 > 2, we return True.

For nums = [5, 4, 3, 2, 1]:
first = inf, second = inf
Iterating through the array:
For 5: first = 5, second = inf
For 4: first = 4, second = inf
For 3: first = 3, second = inf
For 2: first = 2, second = inf
For 1: first = 1, second = inf
No valid triplet is found, so the result is False.
"""
