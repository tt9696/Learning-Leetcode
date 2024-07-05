#
# @lc app=leetcode id=169 lang=python
#
# [169] Majority Element
#
from collections import Counter
# @lc code=start
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = Counter(nums) #Output: Counter({1: 3, 2: 2})
        return max(counts.keys(), key=counts.get) #print(counts.keys()) #dict_keys([1,2])
        #  key=counts.get get the value associated with that key.
        
        # Other answer
        # candidate=nums[0]
        # count=1 #tracks the count of candidate
        # i=1 # start from 2nd element, since first element is already being counted
        # while i < len(nums):
        #     if nums[i]==candidate:
        #         count+=1
        #     elif nums[i]!=candidate and count>=1:
        #         count-=1
        #     elif nums[i]!=candidate and count==0:
        #         candidate=nums[i]
        #         count=1
        #     i+=1
        #   # print(candidate, count)
        # return candidate
        
# @lc code=end

