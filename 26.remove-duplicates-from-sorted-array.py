#
# @lc app=leetcode id=26 lang=python
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != nums[j]:
                j = j+1
                nums[j] = nums [i]

        return j+1

        """
        Sample Answer
        nums[:] = sorted(set(nums))
        return len(nums)
         """
# @lc code=end

