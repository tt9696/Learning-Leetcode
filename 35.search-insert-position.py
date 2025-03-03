#
# @lc app=leetcode id=35 lang=python
#
# [35] Search Insert Position
#

# @lc code=start
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # find the where target, if cannot find, estimate which index it should insert
        # Binary search
        right = len(nums) - 1
        left = 0
        
        while left <= right:
            mid = (left + right)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1 # target must be in the right half, Search the right half
            else:
                right = mid - 1 # Search the left half

        return left # The correct insertion index

    
# @lc code=end
"""
nums = [1, 3, 5, 6], target = 4

First Iteration:
mid  = 0 + 3 //2 # 1
nums[mid] = nums[1] = 3
nums[mid] = 3 is less than 4 => Move left = mid + 1 = 2 (search right half)

Second Iteration:
left = 2, right = 3
mid = 2+3//2 #2
nums[mid] = nums[2] = 5
nums[mid] = 5 is greater than 4 => Move right = mid - 1 = 1 (search left half)

Loop Ends:
left = 2, right = 1 => left > right, exit the loop.
return left =2 

nums = [1, 3, 5, 6], target = 5
Step	left	right	mid	 nums[mid]	    Action
1️⃣	       0	    3	  1	 nums[1] = 3	3 < 5, so search right (left = 2)
2️⃣	       2	    3	  2	 nums[2] = 5	Found! Return mid = 2

nums = [1, 3, 5, 6], target = 2
Step	left	right	mid	  nums[mid]	    Action
1️⃣	        0	    3	  1	  nums[1] = 3	3 > 2, so search left (right = 0)
2️⃣	        0	    0	  0	  nums[0] = 1	1 < 2, so search right (left = 1)
3️⃣	     Loop ends (left = 1, right = 0)	Return left = 1 (Insert 2 at index 1)			
"""
"""
!!! linear search (O(N) time complexity), which is much slower than binary search (O(log N)).

def searchInsert(nums, target):
    for i in range(len(nums)):  # Linear search
        if nums[i] >= target:
            return i
    return len(nums)  # If target is greater than all elements

"""

