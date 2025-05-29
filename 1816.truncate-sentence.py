#
# @lc app=leetcode id=1816 lang=python
#
# [1816] Truncate Sentence
#

# @lc code=start
class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        result = s.split()[:k]
        return ' '.join(result) # add space for each word
        
# @lc code=end
"""
    result = ''
    word_count = 0

    for i in range(len(s)):
        if s[i] == ' ':
            word_count += 1
            if word_count == k:
                break
        result += s[i]

    return result.strip()

"""
