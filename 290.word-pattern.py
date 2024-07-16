#
# @lc app=leetcode id=290 lang=python
#
# [290] Word Pattern
#

# @lc code=start
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        word = s.split(" ")
        word_to_char, char_to_word = {},{}
        if len(pattern) != len(word):
            return False
        
        for char, w in zip(pattern, word):
            if char in char_to_word and char_to_word[char] != w:
                return False
            if w in word_to_char and word_to_char[w] != char:
                return False


            word_to_char[w] = char
            char_to_word[char] = w
        
        return True
# @lc code=end

