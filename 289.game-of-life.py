#
# @lc app=leetcode id=289 lang=python
#
# [289] Game of Life
# https://www.youtube.com/watch?v=fei4bJQdBUQ

# @lc code=start
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        
        """
        rows, columns = len(board), len(board[0])

        def count_live_neighbor(r,c):
            directions = [(-1,-1),(-1,0),(-1, 1),(0, -1),(0, 1),(1,-1),(1,0),(1, 1)]
            count = 0
            for dr, dc in directions:
                nr = r + dr # row index of the neighboring cell
                nc = c + dc

                #If nr is less than 0, it would be outside the board above the first row
                #If nr is greater than or equal to rows, it would be outside the board below the last row
                if 0 <= nr < rows and 0 <= nc < columns and abs(board[nr][nc]) == 1:
                    count += 1
            return count


        for r in range(rows):
            for c in range(columns):
                live_neighbors = count_live_neighbor(r,c)
                #Rule 1 and 3
                if board[r][c] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[r][c] = -1 # Mark as 'to die'
                #Rule 4
                if board[r][c] == 0 and live_neighbors == 3:
                    board[r][c] = 2 # Mark as 'to live'
                
        for r in range(rows):
            for c in range(columns):
                if board[r][c] == -1:
                    board[r][c] = 0
                if board[r][c] == 2:
                    board[r][c] = 1
        

    """
    Apply the rules using intermediate states:
        Mark live cells that will die with -1.
        Mark dead cells that will become alive with 2.

    directions: move forward/up -1, move backward/down 1
    (-1, -1)  (-1, 0)  (-1, 1)
    (0, -1)   ( C )    (0, 1)
    (1, -1)   (1, 0)   (1, 1)

    abs(board[nr][nc]) == 1:

    board[nr][nc] is the value of the neighboring cell.
    The abs function is used to account for the intermediate states used in the algorithm:
    1 represents a cell that is currently alive.
    -1 represents a cell that was alive but is now marked to die.
    abs(board[nr][nc]) will be 1 if the cell is either currently alive (1) or was alive before but is now marked to die (-1).
    
    
    """

# @lc code=end

