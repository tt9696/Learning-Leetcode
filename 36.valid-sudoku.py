#
# @lc app=leetcode id=36 lang=python
#
# [36] Valid Sudoku
# determine if a given 9x9 Sudoku board is valid according to Sudoku rules. 
# Each row, each column, and each of the nine 3x3 sub-boxes must contain the 
# digits 1-9 without repetition.
# use sets to track the numbers already encountered in each row, column, and 
# 3x3 sub-box as we iterate through the existing Sudoku board. 
# Hase-set

# @lc code=start

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        import collections
        
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                num = board[r][c]

                if num == '.':
                    continue

                if (num in rows[r] or
                    num in cols[c] or
                    num in boxes[(r//3,c//3)]):
                    return False
                
                rows[r].add(num)
                cols[c].add(num)
                boxes[(r//3,c//3)].add(num)

        return True
""""
a - row 4 column 4 //3 => [1,1] is index
b - row 8 column 8 //3 => [2,2] is index
c - row 2 column 2 //3 => [0,0] is index
   key = (r/3,c/3)
            (   0   )   (   1   )   (   2   )
            0   1   2   3   4   5   6   7   8
       ------------------------------------------
        0 |
    0   1 |
        2 |          c
        3 |
    1   4 |                 a
        5 |
        6 |
    2   7 |
        8 |                                  b


    Other:
      # rows = [set() for _ in range(9)] #[set(), set(), set(), set(), set(), set(), set(), set(), set()]
        # columns = [set() for _ in range(9)]
        # boxes = [set() for _ in range(9)]
        # for r in range(9):
        #     for c in range(9):
        #         num = board[r][c]
        #         if num == '.': 
        #             continue #skip empty cell
        #         if num in rows[r]: #check if the number is already in the current row's set
        #             return False
        #         rows[r].add(num)
        #         if num in columns[c]:
        #             return False
        #         columns[c].add(num)
        #         box_index = (r//3)*3 +(c//3)  
        #         if num == boxes[box_index]:
        #             return False
        #         boxes[box_index].add(num)
        #     return True
"""
# @lc code=end

