#
# @lc app=leetcode id=71 lang=python
#
# [71] Simplify Path
#

# @lc code=start
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []

        components = path.split("/")

        for c in components:
            if c == "" or c == ".": 
                continue # Skip empty and current directory components
            elif c == "..":
                if stack: # Only pop if the stack is non-empty
                    stack.pop()
            else:
                stack.append(c) # Push the current directory to the stack
        
        return "/"+"/".join(stack)

"""
path = "/home/"
components = path.split("/") => ['', 'home', '']

Intermediate Stack: ['home', 'foo']
return Output: "/home/foo"


Input: path = "/.../a/../b/c/../d/./"
Output: "/.../b/d"

components = ['', '...', 'a', '..', 'b', 'c', '..', 'd', '.']
(1) Stack: ['...']
(2) Stack: ['...', 'a']
(3) The next component is '..', which means need to move up to the parent directory.
Stack after pop: ['...']
(4) Stack: ['...', 'b']
(5) Stack: ['...', 'b', 'c']
(6) Stack after pop: ['...', 'b']
(7) Stack: ['...', 'b', 'd']

"""
# @lc code=end

