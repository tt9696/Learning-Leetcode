#
# @lc app=leetcode id=496 lang=python
#
# [496] Next Greater Element I
# nums1 is subset of num2, use nums1 to find the next greater num of that num in nums2
# For each element in nums1, find the next greater element in nums2.
# 1. We use nums2 to preprocess and find the next greater number for every element.
# 2. But the actual question only wants the answer for the elements in nums1.


# @lc code=start
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        next_greater = {}
        result = []

        # Step 1: Process nums2 with a stack
        for num in nums2:
            while stack and stack[-1] < num: # 1<3
                smaller = stack.pop() # pop 1
                next_greater[smaller] = num # {1:3} # Map `smaller` to its next greater `num`
            stack.append(num)

        # Step 2: Assign -1 for elements with no next greater
        for num in stack: #[4,2]
            next_greater[num] = -1 # next_greater = {1: 3, 3: 4, 4: -1, 2: -1}

        for num in nums1: #[4, 1, 2]
            result.append(next_greater[num]) # next_greater[4] = -1 , result = [-1], result = [3], result = [-1]
        return result # [-1, 3,-1]

# @lc code=end
"""
Approach 1: Brute Force (Nested Loops)
A simple way to solve this problem is:

1. For each number num in nums1, find its position in nums2.
2. Start searching to the right in nums2 for a greater number.
3. If found, return that number; otherwise, return -1.

def nextGreaterElement(nums1, nums2):
    result = []
    
    for num in nums1:
        found = False
        for j in range(nums2.index(num) + 1, len(nums2)):  # Search to the right
            if nums2[j] > num:
                result.append(nums2[j])
                found = True
                break
        if not found:
            result.append(-1)
    return result

✅ Works correctly, but inefficient!

"""
"""
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]

Step	Current Number     Stack                       Next Greater Map
       (num from nums2)   (Stores decreasing numbers)  (next_greater)
1	        1	   append   [1]	                      {}
2	        3  1<3 while    [] (pop 1) → [3]	      {1: 3} (1 → 3 is next greater)
3	        4	   while    [] (pop 3) → [4]	      {1: 3, 3: 4} (3 → 4 is next greater)
4	        2	   append   [4, 2]	                  {1: 3, 3: 4} (4 has no greater yet)

next_greater = {1: 3, 3: 4, 4: -1, 2: -1}
result = [-1, 3, -1]
"""