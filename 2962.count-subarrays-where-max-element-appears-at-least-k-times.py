#
# @lc app=leetcode id=2962 lang=python
#
# [2962] Count Subarrays Where Max Element Appears at Least K Times
# the subarray that contain maximum num 
# https://www.youtube.com/watch?v=CZ-z1ViskzE&t=302s&ab_channel=NeetCodeIO

# @lc code=start
class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_element = max(nums)
        result = 0
        count = 0
        left = 0

        for right in range(len(nums)):
            if nums[right] == max_element:
                count += 1
            while count >= k: # the window is valid 
                result += len(nums) - right

                if nums[left] == max_element:
                    # It tracks how many times the max element appears 
                    # in the current window. When the left pointer removes 
                    # a max_element, we must decrease the count to avoid 
                    # overcounting invalid subarrays.
                    count -= 1
                left += 1
        return result
        
# @lc code=end
"""
nums = [1, 3, 3, 2, 3]
k = 2
max_element = 3
Need count all subarrays with at least 2 '3's

Iterate right from 0 to 4:
right = 0, nums[0] = 1
Not max, count stays 0
count < k → skip

right = 1, nums[1] = 3
It's max → count = 1
count < k → skip

right = 2, nums[2] = 3
Max → count = 2
count >= k ✅
nums[left] = 1 ≠ 3 → no change to count
left = 1
→ Add len(nums) - right = 5 - 2 = 3
res = 3 (subarrays: [1,3,3], [1,3,3,2], [1,3,3,2,3])

right = 3  (nums[3] = 2)
Not max → count unchanged
✅ Still count >= k
→ Add len(nums) - right = 5 - 3 = 2
nums[left] = 3 → yes, count -= 1 = 1
left = 2
res = 5 (subarrays: [3,3,2], [3,3,2,3])

right = 4 (nums[4] = 3)
Max, count += 1 → count = 3
✅ Still count >= k
→ Add len(nums) - right = 5 - 4 = 1
Check nums[left] = 3 → count -= 1 = 1, left = 3
res = 6 (subarray: [3,2,3])

"""
