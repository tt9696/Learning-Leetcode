#
# @lc app=leetcode id=997 lang=python
#
# [997] Find the Town Judge
# Given a list trust[i] = [a, b] meaning person a trusts person b, find the judge if they exist.
# https://www.youtube.com/watch?v=QiGaxdUINJ8&ab_channel=NeetCodeIO
"""
We can track in-degrees and out-degrees for each person:
    - If person i trusts someone, increase their out-degree.    
    - If person i is trusted by someone, increase their in-degree.

The judge should have:
    in-degree = n - 1 (trusted by everyone else)
    out-degree = 0 (trusts nobody)

"""
from collections import defaultdict
# @lc code=start
class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        # condition of judge
        # incoming = n -1
        # outgoing = 0
        incoming = defaultdict(int) # defaultdict(<class 'int'>, {3: 2})
        outgoing = defaultdict(int)

        for src, dst in trust:
            outgoing[src] += 1
            incoming[dst] += 1 

        for i in range(1, n+1):
            if outgoing[i] == 0 and incoming[i] == n-1:
                return i # find judge
        return -1

# @lc code=end

"""
delta = defaultdict(int) #incoming - outgoing = n -1

for src, dict in trust:
    delta[src] -= 1
    delta[dict] += 1

for i in range(1, n+1):
    if delta[i] == n - 1:
        return i

return -1

"""
"""
n = 3, trust = [[1,3],[2,3]]
1 -> 3, incoming of 3 got 1 ( 3 : 1 ), outgoing of 1 to 3 increment 1(1: 1)
2 -> 3, incoming of 3 got +1 ( 3 : 2 ), outgoing of 2 to 3 increment 1 (2: 1)
incoming        outgoing
1 : 0              1 : 1
2 : 0              2 : 1
3 : 2              3 : 0

output is 3, incoming is n -1 (2) , outgoing is 0

"""