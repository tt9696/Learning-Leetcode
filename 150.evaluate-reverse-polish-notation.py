#
# @lc app=leetcode id=150 lang=python
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        for token in tokens:
            if token in "+-*/":
                a = stack.pop()  # Right operand
                b = stack.pop()  # Left operand
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(b - a)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    # checks whether the division result b / a is non-negative 
                    # Case 1: Positive Division => (b / a) >= 0
                    # Case 2: Negative Division with Truncation Toward Zero
                    stack.append(int(b / a) if (b / a) >= 0 else -(abs(b) // abs(a)))
                    # For b = -7 and a = 3 
                    # b / a = -2.333, which is negative.
                    # Using -(abs(b) // abs(a)), we get -(7 // 3) = -2 (truncating toward zero).
                    # The expression becomes stack.append(-2).
                    # not this stack.append(int(b / a)) 
            else:
                stack.append(int(token))
        
        return stack[0]
        
# @lc code=end
'''
Time Complexity: O(n), where n is the number of tokens, as each token is processed once.
Space Complexity: O(n), since we use a stack to store numbers and intermediate results.

Push 4: stack = [4]
Push 13: stack = [4, 13]
Push 5: stack = [4, 13, 5]
Encounter /:
Pop 5 and 13, then perform integer division (13 / 5), which gives 2 (since integer division truncates toward zero).
Push the result back onto the stack.
stack = [4, 2]
Encounter +:
Pop 2 and 4, then add them (4 + 2 = 6).
Push the result back onto the stack.
stack = [6]

Incorrect Result Without abs Condition
For b = -7 and a = 3:
int(b / a) gives -3, which is incorrect for RPN (the correct answer should be -2).
'''
