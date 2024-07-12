#
# @lc app=leetcode id=73 lang=python
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        first_row_has_zero = any(matrix[0][j] == 0  for j in range(cols)) # False
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(rows))

        # Use first row and first column to mark zero rows and columns
        for i in range(1,rows):
            for j in range(1,cols):
                if matrix[i][j] == 0: #[1][1]
                    matrix[0][j] = 0  # Mark the column to be zeroed
                    matrix[i][0] = 0  # Mark the row to be zeroed

        # Zero out cells based on marks in the first row and column
        for i in range(1, rows): #[1][1]
            for j in range(1, cols):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        # Handling the First Row and Column Separately
        if first_row_has_zero:
            for j in range(cols):
                matrix[0][j] = 0 

        if first_col_has_zero:
            for i in range(rows):
                matrix[i][0] = 0 
        """
                    columns j 
                    0     1    2
        row     0         a
        i       1 (1,0) (1,1)  b
                2  c
                
            matrix[0][j] => row is 0

            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
                |    matrix[0][1] = 0  # Mark the column to be zeroed
                |    matrix[1][0] = 0  # Mark the row to be zeroed
                v
            0  1  2
        0   [1, 0, 1],
        1   [0, 0, 1],
        2   [1, 1, 1]
                |
                v
            [1, 0, 1],
            [0, 0, 0],
            [1, 0, 1]

                            
        For i=1 and j=1:
        a: matrix[0][1] == 0 is true, so set b matrix[1][1] to 0.
        For i=1 and j=2:
        c: matrix[0][2] == 0 is false, but matrix[1][0] == 0 is true, so set matrix[1][2] to 0.
        For i=2 and j=1:
        matrix[0][1] == 0 is true, so set matrix[2][1] to 0.
        For i=2 and j=2:
        matrix[0][2] == 0 is false, and matrix[2][0] == 0 is false, so matrix[2][2] remains 1.
        
        Other solution:
           if not matrix:
            return []
        
        m = len(matrix)
        n = len(matrix[0])
        rowzero = [False] * m
        colzero = [False] * n
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    rowzero[row] = True
                    colzero[col] = True
        for row in range(m):
            for col in range(n):
                if rowzero[row] or colzero[col]:
                    matrix[row][col] = 0
        
        """
# @lc code=end

