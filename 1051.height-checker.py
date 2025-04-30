#
# @lc app=leetcode id=1051 lang=python
#
# [1051] Height Checker
#

# @lc code=start
class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        expected = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count += 1
        return count 
# @lc code=end

