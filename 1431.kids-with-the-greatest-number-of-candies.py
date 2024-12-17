#
# @lc app=leetcode id=1431 lang=python
#
# [1431] Kids With the Greatest Number of Candies
#

# @lc code=start
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_candies = max(candies)

        output = []

        for candy in candies:
            if candy+extraCandies >= max_candies:
                output.append(True)
            else:
                output.append(False)
        return output
# @lc code=end

