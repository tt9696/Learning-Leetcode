#
# @lc app=leetcode id=394 lang=python
#
# [394] Decode String
#

# @lc code=start
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        current_s = ""
        current_num = 0
        # s = "3[a2[c]]" Output =  "accaccacc"
        for char in s:
            if char.isdigit():
                # for second also digit 
                current_num = current_num*10 +int(char)  # 0 * 10 + 3 = 3
            elif char == "[":
                stack.append((current_s, current_num))# stack = [('', 3)] , stack = [('', 3), ('a', 2)]
                # reset
                current_s = ""
                current_num = 0
            elif char == "]":
                prev_s , prev_num = stack.pop()
                current_s = prev_s + prev_num * current_s # a + 2 * c
            else:
                current_s += char #a
        
        return current_s 
        
# @lc code=end
"""
'3' → current_num = 3
'[' → Push (current_str, current_num) onto the stack → stack = [('', 3)], reset current_str = "", current_num = 0
'a' → current_str = "a"
'2' → current_num = 2
'[' → Push (current_str, current_num) onto the stack → stack = [('', 3), ('a', 2)], reset current_str = "", current_num = 0
'c' → current_str = "c"
']' → Pop ('a', 2) from stack, repeat "c" twice → current_str = "acc"
']' → Pop ('', 3) from stack, repeat "acc" three times → current_str = "accaccacc"
Final result: "accaccacc"

"""

