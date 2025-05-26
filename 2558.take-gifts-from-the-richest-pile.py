#
# @lc app=leetcode id=2558 lang=python
#
# [2558] Take Gifts From the Richest Pile
#

# @lc code=start
import math
class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        def isqrt(n):
            return int(n ** 0.5)
        
        for _ in range(k):
            max_index = gifts.index(max(gifts)) #gifts.index(64) → 1 (because 64 is at index 1)
            gifts[max_index] = isqrt(gifts[max_index])
        return sum(gifts)
        #   Max = 64 at index 1 → √64 = 8
        # → gifts = [25, 8, 9, 4]
# @lc code=end
"""
    max_heap = [-g for g in gifts] #Max = 64 → √64 = 8 max_heap = [-25, -64, -9, -4]

    heapq.heapify(max_heap) # [-64, -25, -9, -4]

    for _ in range(k):
        richest = -heapq.heappop(max_heap) #-(-64) = 64,  [-25, -4, -9]
        updated = math.isqrt(richest) #8
        heapq.heappush(max_heap, -updated) #pushing -8 , [-25, -8, -9, -4]

    return -sum(max_heap)
"""
