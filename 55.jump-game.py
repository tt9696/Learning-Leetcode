#
# @lc app=leetcode id=55 lang=python
#
# [55] Jump Game
# to keep track of the farthest position that can be reached while iterating through the array. If at any point the current index is beyond the farthest position, it means we cannot proceed further

"""
nums = [2, 3, 1, 1, 4] len(nums)=5
-> nums[0] = 2 can jump 1 step or 2 step
-> if jump 1 step : nums[1]=3  (0 -> 1 -> 4 )
-> if jump 2 step : nums[2]=1  (0 -> 2 -> 3 -> 4) 
"""
# @lc code=start
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxReach = 0 
        for i in range(len(nums)):#i = [0,1,2,3,4]
            if  maxReach < i:
                return False 
            # Update the farthest point we can reach
            maxReach = max(maxReach, i+nums[i])
            
            if maxReach >= len(nums) - 1 : # If reach or exceed the last index, return True len(nums)-1 = 4 maxReach reach index = 4
                return True
    
        return maxReach >= len(nums) - 1 #True
        """
        maxReach = nums[0]
        for i,j in enumerate(nums):
            if maxReach < i:
                return False
            maxReach = max(maxReach, i+j)
        return True"""
# @lc code=end

