#
# @lc app=leetcode id=383 lang=python
#
# [383] Ransom Note
#

# @lc code=start
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        from collections import Counter

        magazine_count = Counter(magazine)#Counter({'a': 2, 'b': 1}) 
        for char in ransomNote:
            if magazine_count[char] > 0:
                magazine_count[char] -= 1 #If yes (magazine_count[char] > 0), decrement the count (since we're using that character).
            else:
                return False
        return True
        
       
# @lc code=end

