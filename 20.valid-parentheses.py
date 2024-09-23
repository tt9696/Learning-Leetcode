#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
# https://www.youtube.com/watch?v=WTzjTskDFMg

# @lc code=start 
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # s = "()[]{}"
        stack = []
        bracket_map = {')':'(','}':'{', ']':'['}
        for char in s:
            if char in bracket_map: # If the current character is a closing bracket 
                if stack and stack[-1] == bracket_map[char]: #check stack is empty and retrieves the top (last) element of the stack
                    stack.pop()
                else:
                    return False
            else: 
                stack.append(char)
        return True if not stack else False #check stack is empty

        
# @lc code=end
'''
 s = "()[]{}"

1. stack = ['(']
2. bracket_map[')'] == '(' => stack = []
3. stack = ['[']
4. bracket_map[']'] == '[' => stack = []
5. stack = ['{']
6. bracket_map['}'] == '{' => stack = []
'''

