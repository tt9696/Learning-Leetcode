#
# @lc app=leetcode id=1470 lang=python
#
# [1470] Shuffle the Array
# [x1,x2,...,xn,y1,y2,...,yn] become [x1,y1,x2,y2,...,xn,yn]
 
# @lc code=start
class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        result = []
        for i in range(n):#0,1,2,3
            result.append(nums[i]) #0
            result.append(nums[i+n]) #0+3 = result.append(3)
        return result
        # nums = [2,5,1,3,4,7]
        # i=0 -> result = [2, 3]
        # i=1 -> result = [2, 3, 5, 4]
        # i=2 -> result = [2, 3, 5, 4, 1, 7]
# @lc code=end
"""
Shortest version:

def shuffle(nums, n):
    return [nums[i//2] if i % 2 == 0 else nums[n+i//2] for i in range(2*n)]

We loop i from 0 to 2n-1 (2n numbers in total).
For each i:
If i is even (i % 2 == 0), pick an element from the first half (nums[i//2] → x1, x2, x3).
If i is odd, pick an element from the second half (nums[n + i//2] → y1, y2, y3)

result = []
    for i in range(2 * n):
        if i % 2 == 0:
            # i is even: pick from first half
            index = i // 2
            result.append(nums[index])
        else:
            # i is odd: pick from second half
            index = n + (i // 2)
            result.append(nums[index])
    return result
"""
