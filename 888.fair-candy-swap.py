#
# @lc app=leetcode id=888 lang=python
#
# [888] Fair Candy Swap
#

# @lc code=start
class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        
# @lc code=end
"""
Swapping first and then checking if the total is equal would be inefficient because:

Brute Force is Too Slow (O(N × M))
If we try every possible swap between Alice and Bob and then check if their sums are equal, we get O(N × M) complexity.
Example: If aliceSizes = [1,2,5] and bobSizes = [2,4], we would check:
Swap (1,2), (1,4), (2,2), (2,4), (5,2), (5,4) → Too many checks!

"""
