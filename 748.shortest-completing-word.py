#
# @lc app=leetcode id=748 lang=python
#
# [748] Shortest Completing Word
# Letters from licensePlate: s, p, s, t → counted as {'s':2, 'p':1, 't':1}
# "step" → missing an s
# "steps" → has 2 s, 1 p, 1 t ✅
# "stripe" → only 1 s ❌
# "stepple" → ✅ but longer than "steps"
# Output: "steps"

# @lc code=start
class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        from collections import Counter
        letters = []
        
        for c in licensePlate:
            if c.isalpha():
                letters.append(c.lower())
            
        lp_count = Counter(letters)
        # lp_count = Counter(c.lower() for c in licensePlate if c.isalpha())
        # lp_count = {'s': 2, 'p': 1, 't': 1}
        result = None
        for word in words:# steps
            word_count = Counter(word.lower())
            # word_count = {'s': 2, 't': 1, 'e': 1, 'p': 1}
            if all(word_count[c] >= lp_count[c] for c in lp_count):
                # word_count['s'] >= 2 
                # word_count['p'] >= 1
                # word_count['t'] >= 1 
                # all() returns True
                if result is None or len(word) < len(result): # checks if the current word is shorter
                    result = word
        return result
        
# @lc code=end

