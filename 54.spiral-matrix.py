#
# @lc app=leetcode id=54 lang=python
#
# [54] Spiral Matrix
# https://www.youtube.com/watch?v=BJnMZNwUk1M

# @lc code=start
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        left, right = 0 ,len(matrix[0])-1 #0,2
        top, bottom = 0, len(matrix)-1 #0,2
        res = []

        while left <= right and top <= bottom:
            # top row
            for i in range(left, right + 1): #0-3
                res.append(matrix[top][i]) #accesses the i-th element in the top-th row.
            top += 1 # move top down

            # right row
            for i in range(top, bottom + 1):# walk down
                res.append(matrix[i][right]) #accesses the right-th element in the i-th row.
            right -= 1 # move R forward

            if top <= bottom:
                for i in range(right, left-1 , -1): #-1 reverse
                    res.append(matrix[bottom][i])
                bottom -= 1 # move bottom up

            if left <= right:
                for i in range(bottom, top-1, -1):
                    res.append(matrix[i][left])
                left += 1 #move left  

        return res
        
    """
                __L_ ___ _R__ 
Row 0 top       | 1 | 2 | 3 |
Row 1           | 4 | 5 | 6 |
Row 2 bottom    | 7 | 8 | 9 |
    
                __L_ ___ _R__ 
Row 0           | 1 | 2 | 3 |
Row 1 top       | 4 | 5 | 6 |
Row 2 bottom    | 7 | 8 | 9 |    

                __L_ _R_ ___ 
Row 0           | 1 | 2 | 3 |
Row 1 top       | 4 | 5 | 6 |
Row 2 bottom    | 7 | 8 | 9 |  

    Initial boundaries: top=0, bottom=2, left=0, right=2.
    Step 1: Traverse 1, 2, 3 from top row.
    Step 2: Traverse 6, 9 from right column.
    Step 3: Traverse 8, 7 from bottom row.
    Step 4: Traverse 4 from left column.
    Step 5: Traverse 5 from the middle of the matrix.
    """
# @lc code=end

