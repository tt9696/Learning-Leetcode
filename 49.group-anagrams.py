#
# @lc app=leetcode id=49 lang=python
#
# [49] Group Anagrams
#

# @lc code=start
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # strs= ["eat","tea","tan","ate","nat","bat"]
        anagrams = {}
        for word in strs:
            sorted_word = ''.join(sorted(word)) # aet
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word]= [word]

        return list(anagrams.values())

"""
else {'aet': ['eat']}
if   {'aet': ['eat', 'tea']}
else {'aet': ['eat', 'tea'], 'ant': ['tan']}
if   {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan']}
if   {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat']}
else {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']}

"""
        
# @lc code=end

