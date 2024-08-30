#
# @lc app=leetcode id=228 lang=python
#
# [228] Summary Ranges
# Find all integers from a to b (inclusive)  

# @lc code=start
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        # nums = [0, 2, 3, 4, 6, 8, 9]
        if not nums:
            return [] 
        
        ranges = []
        start = nums[0] # 0
        for i in range(1, len(nums)):
            # Check if the current number is not consecutive
            if nums[i] != nums[i - 1] + 1: #2 != 1
                # Append the range to the result
                if start == nums[i - 1]:
                    ranges.append(str(start))
                else:
                    ranges.append("{}->{}".format(start, nums[i - 1])) 
                # Start a new range
                start = nums[i]
        
        # Add the last range
        if start == nums[-1]:
            ranges.append(str(start))
        else:
            ranges.append("{}->{}".format(start, nums[-1])) 
    
        return ranges
            
        
# @lc code=end
'''
Iteration:

i = 1: nums[1] = 2 is not consecutive to 0, so add "0" to ranges, start new range at 2.
i = 2: 3 is consecutive to 2, extend range.
i = 3: 4 is consecutive to 3, extend range.
i = 4: 6 is not consecutive to 4, so add "2->4" to ranges, start new range at 6.
i = 5: 8 is not consecutive to 6, so add "6" to ranges, start new range at 8.
i = 6: 9 is consecutive to 8, extend range.
Final Add:

Add "8->9" to ranges.
Result:

ranges = ["0", "2->4", "6", "8->9"]

'''
