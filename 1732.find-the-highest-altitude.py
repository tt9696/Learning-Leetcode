#
# @lc app=leetcode id=1732 lang=python
#
# [1732] Find the Highest Altitude
#

# @lc code=start
class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        highestAltitude = 0
        currentAltitude = 0 

        for g in gain:
            currentAltitude += g
            highestAltitude = max(highestAltitude, currentAltitude)
        return highestAltitude
        
# @lc code=end

