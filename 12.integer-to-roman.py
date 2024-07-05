#
# @lc app=leetcode id=12 lang=python
#
# [12] Integer to Roman
#

# @lc code=start
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # val = [
        #     (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        #     (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        #     (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        # ]
        # roman_numeral = ""
        # # 3749  
        # for(value, symbol) in val:
        #     while num >= value: #3749 >= 1000
        #         roman_numeral += symbol # M
        #         num -= value #num-1000 = 2000
        
        # return roman_numeral # Output: "MMMDCCXLIX"

        symbol = [['I', 1], ['IV', 4], ['V', 5], ['IX', 9], ['X', 10], 
                  ['XL', 40], ['L', 50], ['XC',90], ['C', 100], ['CD', 400], 
                  ['D', 500], ['CM', 900], ['M', 1000]]
        string = ""
        for char, value in reversed(symbol):
            if num // value:
                count = num // value
                string += count * char  #3*M
                num = num % value #749
        return string

        
# @lc code=end

