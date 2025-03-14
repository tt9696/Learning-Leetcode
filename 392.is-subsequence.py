#
# @lc app=leetcode id=392 lang=python
#
# [392] Is Subsequence
#

# @lc code=start
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0
        j = 0


        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i+=1
            j+=1 #Always increment j to move to the next character in t.
        
        return i == len(s)
    # i is equal to the length of s (3), indicating all characters of s have been found in t in order.

        
# @lc code=end

