#
# @lc app=leetcode id=45 lang=python
#
# [45] Jump Game II
# determine the minimum number of jumps required, without necessarily needing to track the exact indices

# @lc code=start
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps = 0
        current_end = 0 # the farthest index that can be reached with the current number of jumps.
        farthest = 0 # the farthest index that can be reached by making the next jump.

        for i in range(len(nums)-1):
            farthest = max(farthest, i +nums[i])
            if i == current_end: 
                jumps +=1
                current_end = farthest

            if current_end >= len(nums)-1:
                break
        return jumps
    """
    [2, 3, 0, 1, 4]
    nums = 能走的step nums[1] = 3 ,能去index 2,3,4
    Index 0:
    farthest = max(0, 0 + 2) = 2
    This means from index 0, you can jump to either index 1 or index 2. Hence, farthest becomes 2.
    i == current_end (0 == 0), we make a jump:
    Increment jumps to 1.
    Update current_end to farthest, which is 2.
    Now, current_end = 2

    Index 1:
    farthest = max(2, 1 + 3) = 4
    From index 1, you can jump to index 2, 3, or 4. Hence, farthest becomes 4.
    i != current_end (1 != 2), so we do not increment jumps
    """
        
# @lc code=end

