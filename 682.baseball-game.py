#
# @lc app=leetcode id=682 lang=python
#
# [682] Baseball Game
#

# @lc code=start
class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        score = []

        for op in operations:
            if op == "C":
                score.pop() # Remove last score
            elif op == "D":  
                score.append(2*score[-1])# Double last score
            elif op == "+": 
                score.append(score[-1]+score[-2])# Sum last two scores
            else: 
                score.append(int(op))# Convert number string to int and add
        return sum(score)  # total sum
# @lc code=end

