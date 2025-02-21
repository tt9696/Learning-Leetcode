#
# @lc app=leetcode id=2390 lang=python
#
# [2390] Removing Stars From a String
#

# @lc code=start
class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for char in s: #"leet**cod*e"
            if char == '*':
                if stack: # Ensure the stack is not empty before popping
                    stack.pop()
            else:
                stack.append(char)
            
        return ''.join(stack)
# @lc code=end

