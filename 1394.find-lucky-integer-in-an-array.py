#
# @lc app=leetcode id=1394 lang=python
#
# [1394] Find Lucky Integer in an Array
#

# @lc code=start
class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        from collections import Counter
        freq = Counter(arr) # freq = {2: 2, 3: 3}
        lucky = -1 #-1 if no lucky found

        for num in freq:
            if num == freq[num]:
                lucky = max(lucky, num) #need return  largest lucky integer in the array
        return lucky

         
# @lc code=end

