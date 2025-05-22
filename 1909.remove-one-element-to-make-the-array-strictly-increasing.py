#
# @lc app=leetcode id=1909 lang=python
#
# [1909] Remove One Element to Make the Array Strictly Increasing
#

# @lc code=start
class Solution(object):
    def canBeIncreasing(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        removed = 0
        #nums = [1, 2, 10, 5, 7]
        for i in range(1, len(nums)):
            # i = 3
            if nums[i] <= nums[i-1]: #10 > 5 ❌ → decrease found (removed = 1)
                removed += 1
                if removed > 1:
                    return False
                
                # check if we can fix this by removing one element i = 3
                if i == 1 or nums[i] > nums[i - 2]: # nums[3] = 5, nums[1] = 2
                    continue  # can remove nums[i - 1]
                else:
                    nums[i] = nums[i - 1] # remove nums[i]

        return True
# @lc code=end

"""
nums = [2, 3, 1, 2]

i = 2:
Compare nums[1] < nums[2] → 3 < 1 ❌ → Violation detected
    violation = 1
if i == 1 or nums[i] > nums[i - 2]
    nums[2] > nums[0]
    nums[2] = 1, nums[0] = 2, 1 > 2 ❌ → condition fails
sequence is still invalid


nums = [3, 4, 2, 3]
At i = 2, we have:
nums[2] = 2
nums[1] = 4 → ❌ Violation: 2 < 4

if nums[2] > nums[0] → 2 > 3 ❌
can't remove 4, instead we simulate removing 2 by doing:
nums[2] = nums[1] → nums = [3, 4, 4, 3]
"""