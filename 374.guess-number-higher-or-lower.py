#
# @lc app=leetcode id=374 lang=python
#
# [374] Guess Number Higher or Lower
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

def guess(num):
    pick = 6
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1 , n # search range

        while left <= right:
            mid = (left + right)//2
            result = guess(mid)

            if result == 0:# found the num
                return mid
            elif result == -1:# guess too high
                right = mid - 1 #The correct number is smaller than mid, update [left, mid - 1]
            else: # guess too low
                left = mid + 1 #[mid + 1, right]
# @lc code=end
"""
If the hidden number is 6 and n = 10, the search steps might look like:

Mid = (1 + 10) // 2 = 5 → guess(5) = 1 (too low) → search [6, 10]
Mid = (6 + 10) // 2 = 8 → guess(8) = -1 (too high) → search [6, 7]
Mid = (6 + 7) // 2 = 6 → guess(6) = 0 (correct) → Return 6

"""
