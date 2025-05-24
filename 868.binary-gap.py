#
# @lc app=leetcode id=868 lang=python
#
# [868] Binary Gap
#

# @lc code=start
class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Step 1: Convert to binary string (remove '0b' prefix)
        binary_str = bin(n)[2:]
        last_index = None # to store index of last seen '1'
        max_gap = 0 # to store the maximum gap

        for i in range(len(binary_str)):
            if binary_str[i] == '1':
                if last_index is not None:
                    # Found another 1, compute gap
                    current_gap = i - last_index
                    # Update max gap if this one is larger
                    max_gap = max(max_gap, current_gap)
                
                last_index = i # update only when a '1' is found
        return max_gap

# @lc code=end
"""
Example: n = 22
Step 1: bin(22) → '0b10110' → '10110'
Step 2: Walk through '10110'

| Index | Char | What happens? (i-index)   | current_gap | Max Gap |
| ----- | ---- | ------------------------- | ---------   | ------- |
| 0     | 1    | First 1 found → save 0    | -           | 0       |
| 1     | 0    | Skip                      |             |         |
| 2     | 1    | Found 1 → gap = 2 - 0 = 2 | 2           | 2       |
| 3     | 1    | Found 1 → gap = 3 - 2 = 1 | 1           | 2       |
| 4     | 0    | Skip                      |             |         |

🧪 Example: n = 22 → '10110'
"1" are at positions 0, 2, and 3.

First 1: no gap yet → last_index = 0

Second 1 at index 2 → gap = 2 − 0 = 2 → max_gap = 2

Third 1 at index 3 → gap = 3 − 2 = 1 → max_gap stays 2

✅ So it returns 2 — correct.
"""
"""
Let’s say n = 22.

Binary of 22 is: 10110
n >>= 1
Before: 10110  (which is 22)
After:  1011   (which is 11)
"""
"""
       prev = None
        max_gap = 0
        index = 0
        while n > 0:
            if n & 1:# bitwise AND 
                if prev is not None:
                    max_gap = max(max_gap, index- prev)
                prev = index
            n >>= 1  # move to next bit
            index += 1
        return max_gap

"""