#
# @lc app=leetcode id=804 lang=python
#
# [804] Unique Morse Code Words
#

# @lc code=start
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        seen = set()

        for w in words:
            transformation = ''
            for char in w:
                # ordinal to get the Unicode code point (ASCII value)
                # ord('c') - ord('a') = 99 - 97 = 2 → morse[2] = "-.-."
                transformation += morse[ord(char) - ord('a')]
                # transformation = ''.join(morse[ord(c) - ord('a')] for c in word)
            seen.add(transformation)
        
        return len(seen)
# @lc code=end

