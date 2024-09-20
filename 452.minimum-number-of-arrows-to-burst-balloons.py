#
# @lc app=leetcode id=452 lang=python
#
# [452] Minimum Number of Arrows to Burst Balloons
#

# @lc code=start
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # [[10,16],[2,8],[1,6],[7,12]]

        points.sort(key=lambda x:x[1]) # [[1,6], [2,8], [7,12], [10,16]]
        arrows = 1
        end = points[0][1] # End of the first balloon after sorting -> 6

       
        for i in range(1, len(points)):       
            if points[i][0] > end: # Start (2) <= End (6)
                arrows += 1
                end = points[i][1]

        return arrows
        
# @lc code=end

"""
If True: The current balloon cannot be burst by the current arrow, so you need to shoot another arrow.
If False: The current balloon can be burst by the current arrow, so no new arrow is needed.

Second Balloon ([2,8]):
Start (2) <= End (6): => No new arrow

Third Balloon ([7,12])
Start (7) > End (6): =>  Shoot a new arrow
end = 12

Fourth Balloon ([10,16]):
Start (10) <= End (12)  => No new arrow

"""