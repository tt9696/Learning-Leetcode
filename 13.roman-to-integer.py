#
# @lc app=leetcode id=13 lang=python
#
# [13] Roman to Integer
# subtracts smaller values before larger values for specific combinations. 
# process each character individually from right to left and handle the subtraction logic by comparing the current and previous values.
# @lc code=start

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_to_int ={
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000   
        }
        total = 0 
        peer_value = 0

        for char in reversed(s): #IV , IX
            current_value = roman_to_int[char] # 5 #1
            if current_value >= peer_value: # 5>=0
                total += current_value # total=5
            else:
                total -= current_value # total=5-1 = 4 ==> IV, IX ==> Output: 9
            peer_value = current_value # peer_value = 5

        return total


        
# @lc code=end

