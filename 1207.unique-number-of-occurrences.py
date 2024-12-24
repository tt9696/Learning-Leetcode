#
# @lc app=leetcode id=1207 lang=python
#
# [1207] Unique Number of Occurrences
# All frequencies are unique, so the result is true

# @lc code=start
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        frequency = {}
        # Step 1: Count occurrences of each number
        for num in arr:
            frequency[num] = frequency.get(num, 0) + 1

        # Step 2: Check if frequencies are unique
        occurrences = list(frequency.values())
        uniques_occurrence = set(occurrences)

        return len(occurrences) == len(uniques_occurrence)

        
        
# @lc code=end

"""
For num = 1:
frequency.get(1, 0) returns 0 (because 1 is not in the dictionary yet).
Add 1: frequency[1] = 0 + 1 = 1.
Now, frequency = {1: 1}.

For num = 2:
frequency.get(2, 0) returns 0.
Add 1: frequency[2] = 0 + 1 = 1.
Now, frequency = {1: 1, 2: 1}.

For num = 2 again:
frequency.get(2, 0) returns 1 (since 2 is already in the dictionary).
Add 1: frequency[2] = 1 + 1 = 2.
Now, frequency = {1: 1, 2: 2}.

For num = 3:
frequency.get(3, 0) returns 0.
Add 1: frequency[3] = 0 + 1 = 1.
Now, frequency = {1: 1, 2: 2, 3: 1}.

For num = 1 again:
frequency.get(1, 0) returns 1.
Add 1: frequency[1] = 1 + 1 = 2.
Now, frequency = {1: 2, 2: 2, 3: 1}.

For num = 1 again:
frequency.get(1, 0) returns 2.
Add 1: frequency[1] = 2 + 1 = 3.
Now, frequency = {1: 3, 2: 2, 3: 1}.
The final frequency dictionary is: {1: 3, 2: 2, 3: 1}

-------------------------------------------------------------
Alternative Approach with collections.Counter
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr):
        freq = Counter(arr)
        return len(freq.values()) == len(set(freq.values()))
"""

