#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)
        return result
    

    """
    num_index = {}

    for index, num in enumerate(nums):
        complement = target - num

        if complement in num_index:
            return [num_index[complement], index]

        num_index[num] = index

    Iteration 1:
    index = 0, num = 2
    complement = 9 - 2 = 7
    7 is not in num_to_index
    Update num_to_index to {2: 0}
    Iteration 2:

    index = 1, num = 7
    complement = 9 - 7 = 2
    2 is in num_to_index (it's the number from the previous iteration)
    Return indices [0, 1]
    """
# @lc code=end

