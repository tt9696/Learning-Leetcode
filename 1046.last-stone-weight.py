#
# @lc app=leetcode id=1046 lang=python
#
# [1046] Last Stone Weight
# If the stones are equal, both are destroyed.
# If they are not equal, the smaller one is destroyed, 
# and the larger one becomes stone1 - stone2.
# Repeat this until at most one stone is left.
# Return the weight of the last remaining stone, or 0 if all stones are destroyed.

# @lc code=start
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        import heapq
        # stones = [2, 7, 4, 1, 8, 1]
        # Step 1: Invert values to simulate max heap
        stones = [-s for s in stones] # stones = [-2, -7, -4, -1, -8, -1]

        # This transforms the list into a valid min-heap, but since values are negative, it behaves like a max-heap.
        heapq.heapify(stones) #stones = [-8, -7, -4, -1, -2, -1]

        while len(stones) > 1:
            first = -heapq.heappop(stones) #largest
            second = -heapq.heappop(stones) #second largest
            if first != second:
                heapq.heappush(stones, -(first-second))

        return -stones[0] if stones else 0
        
# @lc code=end

"""
 less efficient (O(n log n) per loop vs O(log n) with heap).
 while len(stones)>1 :
    stones.sort() # Sort ascending
    first = stones.pop() # 8
    second = stones.pop() # 7

    if first != second:
        stones.append(first - second)
    
    return stones[0] if stones else 0
"""
"""
use a heap when you need efficient access to the smallest or largest element
in a dynamic collection — especially when elements are added or removed frequently.

import heapq

tasks = []
heapq.heappush(tasks, (2, "write code"))
heapq.heappush(tasks, (1, "study"))
heapq.heappush(tasks, (3, "sleep"))

while tasks:
    priority, task = heapq.heappop(tasks)
    print(task)


"""