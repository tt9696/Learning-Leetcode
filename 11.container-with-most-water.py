#
# @lc app=leetcode id=11 lang=python
#
# [11] Container With Most Water
# calculate area


# @lc code=start
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        """
        Height: The height of the container is determined by the shorter of 
        the two lines at the left and right pointers. This is because water 
        cannot exceed the shorter line, so the effective height is the minimum 
        of the two heights: min(height[left], height[right])
        
        """
        left = 0
        right = len(height)-1
        max_area = 0
        while left < right:
            area = min(height[left],height[right])*(right-left) #height*width
            max_area = max(max_area, area)  # Update max_area if the current area is larger

            if height[left]<height[right]:
                left+=1
            else:
                right -= 1

        return max_area

        
       
# @lc code=end

