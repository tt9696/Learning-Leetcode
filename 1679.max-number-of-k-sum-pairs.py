#
# @lc app=leetcode id=1679 lang=python
#
# [1679] Max Number of K-Sum Pairs
#

# @lc code=start
class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        right = len(nums) -1
        nums.sort()
        currentSum = 0
        operation = 0

        while left < right :
            currentSum = nums[left] + nums[right]
            if currentSum == k:
                operation += 1
                left += 1
                right -= 1
            elif currentSum < k: #To try to find a larger sum, move the left pointer
                left += 1
            else: #To find smaller sum
                right -= 1
        return operation
        # to consider a smaller number
# @lc code=end

