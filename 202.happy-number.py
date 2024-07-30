#
# @lc app=leetcode id=202 lang=python
#
# [202] Happy Number
# https://www.youtube.com/watch?v=ljz85bxOYJ0

# @lc code=start
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def sum_of_square(number):
            total_sum = 0
            while number:
                digit = number % 10 # 19 become 9
                digit = digit ** 2 # square
                total_sum += digit
                number = number//10 # 1
            return total_sum

        seen = set()
        while n not in seen:
            seen.add(n)
            n = sum_of_square(n)
            if n == 1:
                return True
        
        return False


# @lc code=end

