#
# @lc app=leetcode id=205 lang=python
#
# [205] Isomorphic Strings
# https://www.youtube.com/watch?v=7yF-U1hLEqQ

# @lc code=start
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        
        """
        if len(s) != len(t):
            return False
        
        mapS_to_T, mapT_to_S  ={}, {}

        for charS, charT in zip(s,t):# f b
            if charS in mapS_to_T and mapS_to_T[charS] != charT: #already have different mapping 
                return False
            if charT in mapT_to_S and mapT_to_S[charT] != charS:
                return False

            mapS_to_T[charS] = charT # {'f': 'b'}
            mapT_to_S[charT] = charS # {'b': 'f'}

        return True
    
    """
                    t : b   a   r 
        mapT_to_S       |   |   |
                        v   v   v
                    s : f   o   o

                    t : b   a   r
        mapS_to_T       ^   ^   ^
                        |   |   |
                    s : f   o   o
    """
# @lc code=end

