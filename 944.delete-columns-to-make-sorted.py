#
# @lc app=leetcode id=944 lang=python
#
# [944] Delete Columns to Make Sorted
# Input: strs = ["cba", "daf", "ghi"]
# Output: 1
# Explanation: 
# - Column 0: 'c', 'd', 'g' -> OK
# - Column 1: 'b', 'a', 'h' -> NOT sorted, must delete
# - Column 2: 'a', 'f', 'i' -> OK
# Only column 1 is unsorted.

# @lc code=start
class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        delete_count = 0
        for col in range(len(strs[0])):#Characters: 'b', 'a', 'h' 
            for row in range(1, len(strs)): #Column 1 → 'b', 'a', 'h'
                #Compare a (row 1) with b (row 0): a < b → True → Column is not sorted
                if strs[row][col] < strs[row-1][col]: #strs[row - 1][col] is the character above it
                    delete_count += 1
                    break #exit the inner loop early once we detect that a column is not sorted.
        return delete_count

        
# @lc code=end

"""
Index:   0     1     2
       ----  ----  ----
Row 0:  'c'   'b'   'a'
Row 1:  'd'   'a'   'f'
Row 2:  'g'   'h'   'i'

Column 0 (col = 0):
Compare row 1 'd' with row 0 'c': 'd' >= 'c' ✅
Compare row 2 'g' with row 1 'd': 'g' >= 'd' ✅
✅ Column 0 is sorted — do not delete.

Column 1 (col = 1):
Compare row 1 'a' with row 0 'b': 'a' < 'b' ❌
Not sorted, so:  delete Column 1.

Column 2 (col = 2):
Compare row 1 'f' with row 0 'a': 'f' >= 'a' ✅
Compare row 2 'i' with row 1 'f': 'i' >= 'f' ✅
✅ Column 2 is sorted — do not delete.

"""