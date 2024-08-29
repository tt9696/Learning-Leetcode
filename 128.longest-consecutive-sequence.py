#
# @lc app=leetcode id=128 lang=python
#
# [128] Longest Consecutive Sequence
# https://www.youtube.com/watch?v=P6RZZMu_maU

# @lc code=start
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums) # Create a set from the nums list to allow O(1) checks
        longest = 0

        for num in nums:
            # Check if it is the start of a sequence : 1-1 = 0
            if (num-1) not in numSet: # dont have left neighbors
                length_sequence = 0
                while (num + length_sequence) in numSet:
                    length_sequence += 1
                longest = max(longest, length_sequence)

        return longest
# @lc code=end
'''
    numSet = {100, 4, 200, 1, 3, 2}

Iteration 1: num = 100 
(100-1)    99 is not in numSet, so 100 is the start of a new sequence, length_sequence = 0
    while (100 + 0) in numSet:  # 100 is in numSet => length_sequence += 1  => longest = max(0, 1) = 1
    
Iteration 2: num = 4
(4-1), 3 is in numSet, so 4 not the start of a new sequence, skip

Iteration 3: num = 200 => longest = max(1, 1) = 1

Iteration 4: num = 1
0 is not in numSet, so 1 is the start of a new sequence.

while (1 + 0) in numSet:  # 1 is in numSet
length_sequence += 1  # length_sequence = 1

while (1 + 1) in numSet:  # 2 is in numSet
length_sequence += 1  # length_sequence = 2

while (1 + 2) in numSet:  # 3 is in numSet
length_sequence += 1  # length_sequence = 3

while (1 + 3) in numSet:  # 4 is in numSet
length_sequence += 1  # length_sequence = 4

'''