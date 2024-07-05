#
# @lc app=leetcode id=42 lang=python
#
# [42] Trapping Rain Water
# The key insight here is that the amount of water trapped at any bar 
# is determined by the shorter of the tallest bars to its left and right.
# water trapped is determined by the difference between the current height and the minimum of the left_max and right_max.

# @lc code=start
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # total_water = 0
        # left = 0
        # right = len(height) - 1 #last index
        # left_max = height[left]
        # right_max = height[right]

        # while left < right:
        #     if height[left] <= height[right]:
        #         if height[left] >= left_max: 
        #             left_max = height[left]
        #         else:
        #             total_water += left_max - height[left] #如果现在的bar<=最高的bar就会积水
        #         left += 1 #move next
        #     else:
        #         if height[right] >= right_max:
        #             right_max = height[right]
        #         else:
        #             total_water += right_max - height[right]
        #         right -= 1 #move forward

        # return total_water
        
        n = len(height)

        if n == 0:
            return 0
        
        left = [0] * n
        right = [0] * n

        left[0] = height[0]
        # left = [0,0,0,0,0,0,0,0,0,0,0,0]
        # height = [0,1,0,2,1,0,1,3,2,1,2,1]
        # determine the highest bar on the left of the current bar.
        for i in range(1, n):
            left[i] = max(left[i-1], height[i]) # left[1] = max(left[0], height[1]) = (0,1)
            #left = [0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]
        

        #determine the highest bar on the right of the current bar.
        right[n-1] = height[n-1]
        for i in range(n-2,-1,-1):
            right[i] = max(right[i+1], height[i]) 
            #right = [3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1]
             
        trapped_water = 0
        for i in range(n):#0,1,2,3,4,5,6,7,8,9,10,11,12
            trapped_water += min(left[i], right[i]) - height[i]
            #trapped_water = (0+0+1+0+1+2+1+0+0+1+0+0) = 6

        return trapped_water
"""
First Iteration:
Compare height[left] and height[right]: height[0] (4) <= height[5] (5)
Since height[left] is less than or equal to height[right], we work with the left pointer:
left_max = max(left_max, height[left]) = max(4, 4) = 4
Since height[left] (4) is equal to left_max (4), no water is trapped.
Move left to 1.
State after this iteration:
left = 1, right = 5, left_max = 4, right_max = 5, total_water = 0

Second Iteration:
Compare height[left] and height[right]: height[1] (2) <= height[5] (5)
Since height[left] is less than or equal to height[right], we work with the left pointer:
left_max = max(left_max, height[left]) = max(4, 2) = 4
Since height[left] (2) is less than left_max (4), water trapped is left_max - height[left] = 4 - 2 = 2.
total_water += 2 → total_water = 2
Move left to 2.
"""


# @lc code=end

