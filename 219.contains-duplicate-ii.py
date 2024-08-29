#
# @lc app=leetcode id=219 lang=python
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # use a sliding window approach with a hash map 
       

        num_dict = {}
        for i, num in enumerate(nums):
            if num in num_dict and i - num_dict[num] <= k:
                return True
            num_dict[num] = i

        return False



# @lc code=end

'''
For nums[0] and nums[2]:
Indices are 0 and 2.
The absolute difference between these indices is |0 - 2| = 2, 
which is greater than k = 1.

 nums =    [1,2,3,1,2,3] k=2
  i   =     0 1 2 3 4 5

  num = 1 ,i = 0 => not => nums_dict = {1: 0}
  num = 2 ,i = 1 => not => nums_dict = {1: 0, 2: 1}
  num = 3 ,i = 2 => not => nums_dict = {1: 0, 2: 1, 3:2}
  num = 1 ,i = 3 => yes => i - num_dict[num] (num_dict[1]=0) = 3-0 = 3 >= k
  num = 2 ,i = 4 => yes => i - num_dict[num] (num_dict[2]=1) = 4-1 = 3 >= k
  num = 3 ,i = 5 => yes => i - num_dict[num] (num_dict[3]=2) = 5-2 = 3 >= k
  False

'''