#
# @lc app=leetcode id=1002 lang=python
#
# [1002] Find Common Characters
# https://www.youtube.com/watch?v=QEESBA2Q_88&ab_channel=NeetCodeIO

# @lc code=start
class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        from collections import  Counter
        count = Counter(words[0]) # count = {'b': 1, 'e': 1, 'l': 2, 'a': 1}
        for w in words:
            current_count = Counter(w)
            for c in count: 
                count[c] = min(count[c], current_count[c])
                # First Iteration (for word "bella"):
                # current_count = {'b': 1, 'e': 1, 'l': 2, 'a': 1}

                # Second Iteration (for word "label"):
                # current_count = {'l': 1, 'a': 1, 'b': 1, 'e': 1}
                # 'b': min(1, 1) → count['b'] = 1
                # 'e': min(1, 1) → count['e'] = 1
                # 'l': min(2, 1) → count['l'] = 1
                # 'a': min(1, 1) → count['a'] = 1
                # New count = {'b': 1, 'e': 1, 'l': 1, 'a': 1}

                # Third Iteration (for word "roller"):
                # current_count = Counter("roller") → current_count = {'r': 2, 'o': 1, 'l': 2, 'e': 1}
                # Updating the counts:
                # 'b': min(1, 0) → count['b'] = 0 (No 'b' in "roller")
                # 'e': min(1, 1) → count['e'] = 1
                # 'l': min(1, 2) → count['l'] = 1
                # 'a': min(1, 0) → count['a'] = 0 (No 'a' in "roller")
                # New count = {'b': 0, 'e': 1, 'l': 1, 'a': 0}
        result = []
        for c in count:
           result.extend([c] * count[c])  # Add 'c' count[c] times to result
        return result
        # Loop through count:
        # 'b' appears 0 times, so skip.
        # 'e' appears 1 time, add 'e' to result: result = ['e']
        # 'l' appears 1 time, add 'l' to result: result = ['e', 'l']
        # 'a' appears 0 times, so skip.
# @lc code=end
"""
Not efficient
def commonChars(words):
    result = []
    for ch in set(words[0]): # set("bella") = {'b', 'e', 'l', 'a'}
        min_count = min(word.count(ch) for word in words)
        result.extend([ch] * min_count)
    return result

For each character in set:
    'b': Appears 1 time in each word.
    min_count = 1
    Add 'b' 1 time to result: result = ['b']
    'e': Appears 1 time in each word.
    min_count = 1
    Add 'e' 1 time to result: result = ['b', 'e']
    'l': Appears 2 times in the first word, 1 time in the second, and 2 times in the third.
    min_count = 1
    Add 'l' 1 time to result: result = ['b', 'e', 'l']
    'a': Appears 1 time in the first and second word, and 0 times in the third word.
    min_count = 0
    Don't add 'a' to the result.
    Final result: ['b', 'e', 'l']
----------------------------------------------------------------------------
Manual Frequency Arrays (26 letters)
def commonChars(words):
    min_freq = [float('inf')] * 26  # Initialize min frequencies

    for word in words:
        freq = [0] * 26  # Frequency of current word
        for ch in word:
            freq[ord(ch) - ord('a')] += 1 #'a' has a Unicode code point of 97.

        for i in range(26):
            min_freq[i] = min(min_freq[i], freq[i])

    result = []
    for i in range(26):
        result.extend([chr(i + ord('a'))] * min_freq[i])

    return result
--------------------------- ------------------------------
    common = Counter(words[0]) # words[0] is "bella", Counter({'l': 2, 'b': 1, 'e': 1, 'a': 1})

    for word in words[1:]: # "label"
        #in both Counter, freq is 1, take the minimum count between the two 
        common &= Counter(word) # Counter({'l': 1, 'a': 1, 'b': 1, 'e': 1})

    result = []
    for char, freq in common.items():#dict_items([('b', 1), ('e', 1), ('l', 2), ('a', 1)])
        result.extend([char]*freq)#result.extend(['b']) → result = ['b']
        # For 'l' (freq = 2):
        # [char] * freq → ['l', 'l']
        # result.extend(['l', 'l']) → result = ['b', 'e', 'l', 'l']
    return result
    """
