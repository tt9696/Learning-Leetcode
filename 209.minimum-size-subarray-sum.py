#
# @lc app=leetcode id=209 lang=python
#
# [209] Minimum Size Subarray Sum
# Sliding Window method

# @lc code=start
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        #nums = [2, 3, 1, 2, 4, 3]
        #target = 7
        n = len(nums) 
        min_length = float('inf') #min_length = infinity
        current_sum = 0
        start = 0

        for end in range(n): #0 to 5
            current_sum += nums[end] # 2 5 6 8

            while current_sum >= target:
                min_length = min(min_length, end - start + 1) #min_length = min(infinity, 4) = 4 #end - start + 1 = size of window
                
                #  need move pointer to next, the left (initial pointer can delete)
                current_sum -= nums[start] #nums[start] = 2 =>(8-2), current_sum = 6
                start += 1

        return 0 if min_length == float('inf') else min_length

"""
Index:   0    1    2    3    4    5
        [2,   3,   1,   2,   4,   3]
              ^         ^
            start      end
subarray from index 1 to index 3 includes the elements [3, 1, 2]
num_element = inclusive counting: end - start + 1
"""
# @lc code=end

