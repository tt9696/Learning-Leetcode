#
# @lc app=leetcode id=1752 lang=python
#
# [1752] Check if Array Is Sorted and Rotated

# https://www.youtube.com/watch?v=Vzs_vlCIFEw&ab_channel=NeetCodeIO
# 3 4 5 5 1 2 -> 3 4 5 5 | 1 2 把3 4 5 5 放在 1 2 后面就是sorted了
# 一直compare 前一个数字， check是不是increse, 
# 如果不是increase（1 < 5）, window not valid, count重新reset
# @lc code=start
class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        count = 1

        if n == 1 : return True # always sorted

        # 2* n = 3 4 5 5 1 2 3 4 5 5 1 2
        for i in range(1, 2*n): # start at 1
            if nums[(i-1) % n] <= nums[i % n]: # compare to previous one 3<=4, %n to prevent out of index
                count += 1
            else: #reset
                count = 1 
            if count == n: # window match length of original nums
                return True       
        return False
        
# @lc code=end

"""
    index = 8 
    n = 6
    index%n = 8 % 6 = 2 (original index) 

index     0 1 2 3 4 5 | 6 7 8 9 10 11
          3 4 5 5 1 2 | 3 4 5 5  1  2
                            ^
                    
index     0 1 2 3 4 5 | 6 7 8 9 10 11
          3 4 5 5 1 2 | 3 4 5 5  1  2
              ^              
"""