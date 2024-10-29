#
# @lc app=leetcode id=155 lang=python
#
# [155] Min Stack
#

# @lc code=start
class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minStack = [] # store min value

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        # Push to min_stack if it's empty or val is the new minimum
        if not self.minStack or val <= self.minStack[-1]: # most recent minimum element
            self.minStack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            if self.stack[-1] == self.minStack[-1]: # Popping the Minimum
                self.minStack.pop()
            self.stack.pop()
        
    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1] if self.stack else None # returns the last element in stack
        # return self.stack[-1] if self.stack else None

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1] if self.minStack else None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

