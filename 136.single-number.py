#
# @lc app=leetcode id=136 lang=python
#
# [136] Single Number
#

# @lc code=start
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            result ^= num # XOR all numbers
        return result
    """
    XOR
    4 ^ 1 ^ 2 ^ 1 ^ 2
    = (4 ^ (1 ^ 1) ^ (2 ^ 2))
    = (4 ^ 0 ^ 0)
    = 4
    
    """
# @lc code=end

"""
HashMap - ❌ Downside: Extra O(n) space
from collections import Counter

def singleNumber(nums):
    count = Counter(nums)  # Count occurrences
    for num, freq in count.items():
        if freq == 1:
            return num

Using Sorting – ❌ Downside: Sorting takes O(n log n) time
def singleNumber(nums):
    nums.sort()
    for i in range(0, len(nums)-1, 2):
        if nums[i] != nums[i+1]:
            return nums[i]
    return nums[-1]
"""