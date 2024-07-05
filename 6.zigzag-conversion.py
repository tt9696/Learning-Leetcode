#
# @lc app=leetcode id=6 lang=python
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        
        current_row = 0
        rows= [''] * numRows
        going_down = False 

        for char in s:
            rows[current_row] += char
            if current_row == 0 or current_row == numRows -1 : #top (0) or the bottom (numRows - 1), 
                going_down = not going_down #Change direction when you reach the top or bottom row. 
            
            if going_down:#(1 for down, -1 for up).
                current_row += 1
            else:
                current_row -= 1
    

        return ''.join(rows)

    """
    current_row = 0
    P: rows = ["P", "", "", ""], going_down = True ,current_row = 1 
    A: rows = ["P", "A", "", ""], going_down = True, current_row = 2
    Y: rows = ["P", "A", "Y", ""], going_down = True, current_row = 3
    P: rows = ["P", "A", "Y", "P"], going_down = False, current_row = 2, 
    A: rows = ["P", "A", "YA", "P"], current_row = 1
    L: rows = ["P", "AL", "YA", "P"], current_row = 0
    I: rows = ["PI", "AL", "YA", "P"], current_row = 1, going_down = True
    S: rows = ["PI", "ALS", "YA", "P"], current_row = 2
    H: rows = ["PI", "ALS", "YAH", "P"], current_row = 3
    I: rows = ["PI", "ALS", "YAH", "PI"], current_row = 2, going_down = False
    R: rows = ["PI", "ALS", "YAHR", "PI"], current_row = 1
    I: rows = ["PI", "ALSI", "YAHR", "PI"], current_row = 0
    N: rows = ["PIN", "ALSI", "YAHR", "PI"], current_row = 1, going_down = True
    G: rows = ["PIN", "ALSIG", "YAHR", "PI"], current_row = 2

    
    """

# @lc code=end

