#
# @lc app=leetcode id=575 lang=python
#
# [575] Distribute Candies
# Return the maximum number of different types of candies she can get.

# @lc code=start
class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        total_candies = len(candyType)
        half_candies = total_candies // 2  # Alice can take half of the candies
        unique_type = len(set(candyType)) # Count unique candy types
        
        # min(3, 3) = 3
        # min(2, 3) = 2
        return min(unique_type,half_candies) # Max variety Alice can get
        
        # If there are more unique types than half_candies, Alice can only take half_candies types.
        # If there are fewer unique types than half_candies, Alice takes all unique types.

        
# @lc code=end

