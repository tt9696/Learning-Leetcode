#
# @lc app=leetcode id=58 lang=python
#
# [58] Length of Last Word
#

# @lc code=start
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        words = s.split()
        last_word = words[-1]

        return len(last_word)
# @lc code=end

