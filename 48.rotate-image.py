#
# @lc app=leetcode id=48 lang=python
#
# [48] Rotate Image
#

# @lc code=start
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        #len(matrix)=3
            
        for row in range(len(matrix)):# 0-2
            for column in range(row, len(matrix)):#012
                temp = matrix[row][column] # holds the original value of matrix[row][col]
                matrix[row][column] = matrix[column][row]
                matrix[column][row] = temp

        for row in matrix:
            row.reverse()
        
        
            """
            Step 1: Transpose   Step 2: Reverse  
            1 2 3      1 4 7        7, 4, 1
            4 5 6  =>  2 5 8   =>   8, 5, 2
            7 8 9      3 6 9        9, 6, 3

            row = 0 : col = 0: No change, swap matrix[0][0] with matrix[0][0]
                    : col = 1: Swap matrix[0][1] with matrix[1][0]

                    temp = matrix[0][1]  # temp = 2
                    matrix[0][1] = matrix[1][0]  # matrix[0][1] = 4
                    matrix[1][0] = temp  # matrix[1][0] = 2
                        [1, 4, 3],
                        [2, 5, 6],
                        [7, 8, 9]
                    
                    : col = 2: Swap matrix[0][2] with matrix[2][0]
            row = 1 : col = 1: No change, swap matrix[1][1] with matrix[1][1]
                    : col = 2: Swap matrix[1][2] with matrix[2][1]
            row = 2 : col = 2: No change, swap matrix[2][2] with matrix[2][2]        

            
            Other solutions:
                
                matrix[:] = zip(*matrix[::-1])
            """


# @lc code=end

