#
# @lc app=leetcode id=500 lang=python
#
# [500] Keyboard Row
#

# @lc code=start
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        """
        Approach
       1. Define the keyboard rows as sets for quick lookup.

       2. For each word:

          Convert it to lowercase (to handle case insensitivity).

          Check if all characters belong to the same row.

       3. Return the list of valid words.
        """

        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        result = []

        for word in words:
            lower_word = set(word.lower()) #change to lower case

            # set("hello") <= set("qwertyuiop")  # False
            # set("dad") <= set("asdfghjkl")  # True
            # Check if all letters in lower_word subset exist in set row
            
            # "Dad" → {'d', 'a'} (Only row 2 ✅)
            # "Peace" → {'p', 'e', 'a', 'c'} (Uses multiple rows)❌
            if lower_word <= row1 or lower_word <= row2 or lower_word <= row3:
                result.append(word)
        return result
# @lc code=end

