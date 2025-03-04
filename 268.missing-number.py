#
# @lc app=leetcode id=268 lang=python
#
# [268] Missing Number
#

# @lc code=start
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        missing = len(nums)

        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing
    """
    XOR property:
    x ^ x = 0 (Same numbers cancel out)
    x ^ 0 = x (XOR with zero remains unchanged)
    
    missing = 3  (Start with n)
    missing ^= 0 ^ 3 → 3 ^ 0 ^ 3 = 0
    missing ^= 1 ^ 0 → 0 ^ 1 ^ 0 = 1
    missing ^= 2 ^ 1 → 1 ^ 2 ^ 1 = 2
    """
# @lc code=end

"""
1. Using Mathematical Formula (Sum Formula) 
def missingNumber(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

n = 3 → Expected sum = 3 * (3+1) / 2 = 6
Actual sum = 3 + 0 + 1 = 4
Missing number = 6 - 4 = 2 

2. Sorting & Checking:  Downside: Sorting takes O(n log n) time, less efficient.
def missingNumber(nums):
    nums.sort()
    for i in range(len(nums)):
        if nums[i] != i :
            return i
    return len(nums)

"""