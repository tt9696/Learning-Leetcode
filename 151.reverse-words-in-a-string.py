#
# @lc app=leetcode id=151 lang=python
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip() # the sky is blue
        words = s.split() # ['the', 'sky', 'is', 'blue']
        words.reverse() # w = word[::-1] blue is sky the
        words = " ".join(words)
        return words
        
# @lc code=end

