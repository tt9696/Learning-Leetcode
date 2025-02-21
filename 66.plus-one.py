#
# @lc app=leetcode id=66 lang=python
#
# [66] Plus One
#

# @lc code=start
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        # n = 5, range(n-1, -1, -1) will generate the sequence: [4, 3, 2, 1, 0]. 
        # The loop will start with i = 4 and end when i = 0
        for i in range(n-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits 
        # digits = [9, 9, 9] after the loop you get [0, 0, 0], 
        # return [1] + [0, 0, 0]


# @lc code=end

