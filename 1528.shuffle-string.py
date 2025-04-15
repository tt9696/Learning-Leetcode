#
# @lc app=leetcode id=1528 lang=python
#
# [1528] Shuffle String
#

# @lc code=start
class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        result = [''] * len(s) # ['', '', '', '', '', '', '', '']
        # s = "codeleet", indices = [4,5,6,7,0,2,1,3]
        for i in range(len(s)):
            char = s[i] #c
            target_index = indices[i] #4

            result[target_index] = char # result[4] = c

        final_string = ''.join(result)
        return final_string        
# @lc code=end

"""
for i in range(len(s)):
    result[indices[i]] = s[i]  # place s[i] at the right spot
    
return ''.join(result)  # convert list back to string
"""