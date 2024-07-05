#
# @lc app=leetcode id=15 lang=python
#
# [15] 3Sum
#

# @lc code=start
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """
        nums = [-1, 0, 1, 2, -1, -4]:

        After sorting, nums becomes [-4, -1, -1, 0, 1, 2].
        Length of nums is 6 (len(nums) = 6).
        If we iterate with for i in range(len(nums) - 2):

        The loop will iterate i from 0 to 3 (len(nums) - 2 = 4).
        This ensures that the left and right pointers are within valid bounds.
        If we iterate with for i in range(len(nums)) instead:
        When i = 4:
        left = 5, right = 5 (invalid because left is not less than right).
        When i = 5:
        left = 6 (out of bounds).

        After selecting a = nums[i], two pointers (left and right) 
        are initialized to find pairs (b, c) such that b + c = -a.

        In the example [-4, -1, -1, 0, 1, 2], when iterating:
        For i = 0, a = -4, b = -1, c = 2.
        For i = 1, a = -1, b = -1, c = 2.
        For i = 2, a = -1, b = 0, c = 1.
        """
        nums.sort()
        result  =[]
        for i in range(len(nums)-2): # 0,1,2,3
            if i > 0 and nums[i] == nums[i - 1]:
                continue # Skip duplicate values of nums[i]

            left = i+1 # Start just after i
            right = len(nums)-1

            while left < right:
                sum_abc = nums[i] + nums[left] + nums[right]

                if sum_abc == 0:
                    #handle the triplet, then adjust left and right pointers
                    result.append([nums[i], nums[left], nums[right]])
                    # Skip duplicates for b and c
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif sum_abc < 0:
                    left += 1
                else:
                    right -= 1   
        return result 

         #efficiently find pairs (b, c) for a given a = nums[i], such that the sum a + b + c = 0. 


# @lc code=end

