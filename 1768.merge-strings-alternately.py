#
# @lc app=leetcode id=1768 lang=python
#
# [1768] Merge Strings Alternately
#

# @lc code=start
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = []
        i, j = 0, 0

        # Merge alternating characters from both strings
        while i < len(word1) and j < len(word2):
            merged.append(word1[i])
            merged.append(word2[j])
            i += 1
            j += 1

        # Add any remaining characters
        if i < len(word1):
            merged.append(word1[i:])
         # Add any remaining characters
        if j < len(word2):
            merged.append(word2[j:])
    
        return ''.join(merged) # Output:"apbqcd"

# @lc code=end

