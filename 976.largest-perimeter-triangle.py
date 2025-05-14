#
# @lc app=leetcode id=976 lang=python
#
# [976] Largest Perimeter Triangle
# (For all combinations: a + b > c, a + c > b, b + c > a)

# @lc code=start
class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #nums = [2, 1, 2]
        nums.sort(reverse=True) # After sorting: [2, 2, 1] descending
        perimeter = 0
        # len(nums=4) => range(len(nums) - 2) = range(2) → i = 0, 1
        for i in range(len(nums)-2):# without going out of bounds.
            if nums[i] < nums[i+1] + nums[i+2]:# Check: 2 < 2 + 1 → ✅ valid triangle
                perimeter = nums[i] + nums[i+1] + nums[i+2]
                return perimeter # Return 2 + 2 + 1 = 5
        return 0

# @lc code=end

