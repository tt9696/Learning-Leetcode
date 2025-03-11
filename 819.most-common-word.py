#
# @lc app=leetcode id=819 lang=python
#
# [819] Most Common Word
#

# @lc code=start
import re
from collections import Counter

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = paragraph.lower() # convert all to lower case
        words = re.findall(r'\w+', paragraph) # Extract words, removing punctuation [a-zA-Z0-9_]

        banned_set = set(banned) # banned_set = {"hit"}  

        word_count = Counter()
        for word in words:
            if word not in banned_set:
                word_count[word] += 1
        #{
        #   "bob": 1,
        #   "a": 1,
        #   "ball": 2,  # Most frequent
        #   "the": 1,
        #   "flew": 1,
        #   "far": 1
        # }

        return max(word_count, key=word_count.get)
        # Input: {"bob": 1, "ball": 2, "a": 1, "the": 1}
        # Output: "ball"

# @lc code=end

"""
import re

text = "Hello, world! This is a test."
words = re.findall(r'\w+', text)

Output: ['Hello', 'world', 'This', 'is', 'a', 'test']

re.findall(r'\w', paragraph) → Extracts single characters
"""