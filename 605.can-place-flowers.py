#
# @lc app=leetcode id=605 lang=python
#
# [605] Can Place Flowers
#

# @lc code=start
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        length = len(flowerbed)

        for i  in range(length):
            if flowerbed[i] == 0: # Ensures the current spot is empty
                # For i == 0: Ignore the left neighbor, check only the right neighbor. (start of array)
                # For i == length - 1: Ignore the right neighbor, check only the left neighbor (end of array)
                if (i == 0 or flowerbed[i-1] == 0) and (i == length - 1 or flowerbed[i+1] == 0):
                    # Plant a flower at current position
                    flowerbed[i] = 1
                    n -= 1 # One less flower to plant

                    if n == 0: # All flowers are planted
                        return True
    # means there are still flowers that could not be planted because there wasn't enough space.  
        return n <= 0 

"""
flowerbed = [0, 0, 0, 0, 0]
n = 2

i = 0 (start of array):
i == 0: No left neighbor, check only flowerbed[1].
flowerbed[1] == 0 → Plant a flower at i = 0.

i = 4 (end of array):
i == length - 1: No right neighbor, check only flowerbed[3].
flowerbed[3] == 0 → Plant a flower at i = 4.

Final flowerbed: [1, 0, 0, 0, 1].
"""

# @lc code=end

