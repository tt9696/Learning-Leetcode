#
# @lc app=leetcode id=389 lang=python
#
# [389] Find the Difference
#

# @lc code=start
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        result = 0
        for char in s+t:
            # bitwise XOR all characters together
            result ^= ord(char) # ord() Convert each character to its ASCII value
        
        return chr(result) #Convert the result back to a character
        
    '''
    Use Counter

        count_s, count_t = Counter(s), Counter(t)

        for char in count_t:
            if count_t[char] != count_s.get(char, 0):
                return char
    '''
# @lc code=end

"""
0 ^ 0 = 0
1 ^ 1 = 0
0 ^ 1 = 1
1 ^ 0 = 1

Character: a, ASCII: 97, Result before XOR: 0
Result after XOR: 97

Character: b, ASCII: 98, Result before XOR: 97
Result after XOR: 3

Character: c, ASCII: 99, Result before XOR: 3
Result after XOR: 96

Character: d, ASCII: 100, Result before XOR: 96
Result after XOR: 4

Character: a, ASCII: 97, Result before XOR: 4
Result after XOR: 101

Character: b, ASCII: 98, Result before XOR: 101
Result after XOR: 7

Character: c, ASCII: 99, Result before XOR: 7
Result after XOR: 100

Character: d, ASCII: 100, Result before XOR: 100
Result after XOR: 0

Character: e, ASCII: 101, Result before XOR: 0
Result after XOR: 101

Final Result (ASCII): 101, Character: e

"""

