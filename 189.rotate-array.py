#
# @lc app=leetcode id=189 lang=python
#
# [189] Rotate Array
#

# @lc code=start
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k %= len(nums) # k = 3 % 7 results in k = 3 (since 3 is already within the bounds, it remains the same). when k is large than array 7%5=2
        nums = nums[-k:] + nums[:-k]
      
        #print(nums[:-3]) Output:[1,2,3,4]

# @lc code=end

