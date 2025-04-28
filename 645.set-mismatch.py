#
# @lc app=leetcode id=645 lang=python
#
# [645] Set Mismatch
# find both the duplicated and missing numbers and return them as a list [duplicate, missing].

# @lc code=start
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        counter = Counter(nums)
        #Safer for debugging. Catches mistakes clearly.
        duplicate = missing = -1 #-1 is never a valid number in this problem (numbers are only from 1 to n).

        for num in range(1, len(nums)+1): #Loops 1 to n， +1 to include last number
            #print(num) prints 1, 2  (numbers to check)
            if counter[num] == 2:
                duplicate = num
            elif counter[num] == 0:
                missing = num
        return [duplicate, missing]
        
# @lc code=end

"""
[1,2,2,4]
n = len(nums) # 4
expected_sum = n * (n + 1)//2 # 4×5/2 = 10
actual_sum = sum(nums) #9
actual_set_sum = sum(set(nums))

duplicate = actual_sum - actual_set_sum
missing = expected_sum - actual_set_sum

return [duplicate, missing]
"""