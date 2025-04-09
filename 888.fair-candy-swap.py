#
# @lc app=leetcode id=888 lang=python
#
# [888] Fair Candy Swap
# Find one pair of candies (x from Alice, y from Bob) such that:
# sum(A) - x + y == sum(B) - y + x
# exchange one candy box each so that after the exchange, they both have the same total amount of candy.

# @lc code=start
class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        sumA = sum(aliceSizes)
        sumB = sum(bobSizes)
        diff = (sumB - sumA) // 2
        bobSet = set(bobSizes)

        # Alice needs to give away a candy that is diff bigger than what she gets.
        for x in aliceSizes:
            y = x + diff
            if y in bobSet: # Make sure Bob actually has the matching candy.
                return [x, y]
        """
        A = [1, 2]
        B = [2, 3]
        sumA = 3
        sumB = 5
        difference = (3 - 5) // 2 = -1

        That means: Alice needs to take a candy 1 bigger than what she gives.

        Try:
        - x = 1 → y = 2 ❌ (2 not in B)
        - x = 2 → y = 3 ✅ (3 is in B)

So return [2, 3]
        """
# @lc code=end
"""
Swapping first and then checking if the total is equal would be inefficient because:

Brute Force is Too Slow (O(N × M))
If we try every possible swap between Alice and Bob and then check if their sums are equal, we get O(N × M) complexity.
Example: If aliceSizes = [1,2,5] and bobSizes = [2,4], we would check:
Swap (1,2), (1,4), (2,2), (2,4), (5,2), (5,4) → Too many checks!
---------------------------------------------------------------
Alice gives away x, and Bob gives away y.
After swapping, Alice gains y and Bob gains x.
The new sums should be equal:
            sumA-x+y = sumB-y+x
        
Simplifies to:
            y = x+(sumB-sumA)/2

Let diff = (sumB - sumA) / 2

aliceSizes = [1,2,5]
bobSizes = [2,4]
sumA = 1 + 2 + 5 = 8
sumB = 2 + 4 = 6
diff = (sumB - sumA) // 2 = (6 - 8) // 2 = -1
We check for y = x - 1
Alice can give 5, Bob can give 4
Swap (5, 4)
✅ Valid swap → New sums are both 7.
"""
